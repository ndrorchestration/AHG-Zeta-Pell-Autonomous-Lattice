# Security Policy

This repository is a public experimental research artifact. It must not contain live credentials, private keys, access tokens, recovery material, or other secrets.

## Credential handling

- Store credentials only in an appropriate secret manager or runtime environment mechanism.
- Colab notebooks must read credentials from Colab Secrets or an equivalent injected environment mechanism; never hard-code them into notebook cells.
- GitHub Actions must use repository/environment secrets through the Actions secret context rather than literal credential values.
- Local development files containing credentials must remain untracked.
- Generated exports, notebooks, logs, and debug bundles must be checked before they are committed.

## Repository guard

`Credential History Guard` scans every unique text blob reachable from the checked-out Git history for several common credential signatures. The workflow intentionally reports only the commit, path, and credential class; it does not print the candidate secret value.

The guard is fail-closed for text blobs larger than its inspection limit rather than silently declaring them clean.

## Incident response

If a credential is ever committed or otherwise exposed:

1. Revoke or disable the exposed credential immediately.
2. Rotate it and any dependent credentials when appropriate.
3. Remove the credential from the current source and from reachable Git history if it entered the repository.
4. Re-run the credential-history guard and any provider-native secret scanning available for the repository.
5. Review generated artifacts and external mirrors for the same value.

Deleting or editing only the newest copy is not sufficient when a secret may remain in version history.

Do not paste a suspected live credential into a public issue, pull request, commit message, or discussion while reporting a problem.
