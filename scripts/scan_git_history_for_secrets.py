#!/usr/bin/env python3
"""Fail closed if secret-like credentials exist in any reachable Git blob."""

from __future__ import annotations

import re
import subprocess
import sys

MAX_TEXT_BLOB_BYTES = 10 * 1024 * 1024

PATTERNS = (
    ("github-classic-pat", re.compile(b"gh" + b"p_[A-Za-z0-9]{20,}")),
    ("github-fine-grained-pat", re.compile(b"github" + b"_pat_[A-Za-z0-9_]{20,}")),
    ("github-oauth-token", re.compile(b"gh" + b"[our]_[A-Za-z0-9]{20,}")),
    ("github-actions-token", re.compile(b"gh" + b"s_[A-Za-z0-9]{20,}")),
    ("aws-access-key", re.compile(b"AKIA[0-9A-Z]{16}")),
    ("npm-token", re.compile(b"npm" + b"_[A-Za-z0-9]{20,}")),
    ("slack-token", re.compile(b"xox" + b"[baprs]-[A-Za-z0-9-]{20,}")),
    ("openai-style-key", re.compile(b"sk" + b"-(?:proj-)?[A-Za-z0-9_-]{20,}")),
    ("private-key-block", re.compile(b"-----BEGIN " + b"(?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
)


def git(*args: str) -> bytes:
    return subprocess.check_output(("git", *args), stderr=subprocess.STDOUT)


def main() -> int:
    try:
        revisions = git("rev-list", "--all").decode("ascii").splitlines()
    except subprocess.CalledProcessError as exc:
        sys.stderr.buffer.write(exc.output)
        return 2

    if not revisions:
        print("No reachable commits found; refusing to report a clean history.", file=sys.stderr)
        return 2

    seen_blobs: set[str] = set()
    findings: list[tuple[str, str, str]] = []
    oversized_text: list[tuple[str, str, int]] = []

    for revision in revisions:
        tree = git("ls-tree", "-r", "-z", revision)
        for raw_entry in tree.split(b"\0"):
            if not raw_entry:
                continue
            metadata, raw_path = raw_entry.split(b"\t", 1)
            _mode, obj_type, blob_sha = metadata.decode("ascii").split()
            if obj_type != "blob" or blob_sha in seen_blobs:
                continue
            seen_blobs.add(blob_sha)
            path = raw_path.decode("utf-8", "surrogateescape")

            size = int(git("cat-file", "-s", blob_sha))
            if size > MAX_TEXT_BLOB_BYTES:
                prefix = git("cat-file", "blob", blob_sha)[:8192]
                if b"\0" not in prefix:
                    oversized_text.append((revision, path, size))
                continue

            data = git("cat-file", "blob", blob_sha)
            if b"\0" in data[:8192]:
                continue

            for label, pattern in PATTERNS:
                if pattern.search(data):
                    findings.append((revision, path, label))

    if oversized_text:
        print("Credential guard cannot silently skip oversized text blobs:", file=sys.stderr)
        for revision, path, size in oversized_text:
            print(f"  {revision[:12]}  {path}  ({size} bytes)", file=sys.stderr)
        return 1

    if findings:
        print("Secret-like credential material detected in reachable Git history.", file=sys.stderr)
        print("Values are intentionally not printed.", file=sys.stderr)
        for revision, path, label in findings:
            print(f"  {revision[:12]}  {path}  [{label}]", file=sys.stderr)
        print("Revoke/rotate the credential and remove it from history before merging.", file=sys.stderr)
        return 1

    print(
        f"Credential guard PASS: scanned {len(seen_blobs)} unique blobs "
        f"across {len(revisions)} reachable commits."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
