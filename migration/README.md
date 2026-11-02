# Pending GitHub Actions permissions

This draft pull request contains the static website and its complete target
workflow in `migration/publish.yaml`. The existing files under
`.github/workflows/` are deliberately unchanged because the available GitHub
credential cannot modify workflows.

**Do not merge this draft until the following changes have been applied on
this branch.** The current deployment workflow still expects Hugo sources.

1. Give the Git credential the `workflow` scope (for a classic personal access
   token), or use a credential with permission to update repository workflows.
   Alternatively, the repository owner can make these edits in GitHub's editor.
2. Replace `.github/workflows/publish.yaml` with `migration/publish.yaml`.
3. Delete `.github/workflows/import-publications.yml` and
   `.github/workflows/updater-wip.yml`; they belong to the retired Hugo setup.
4. Remove this temporary `migration/` directory once the workflow is active.
5. Run `python3 scripts/check_site.py`, check the pull request's GitHub Actions
   result, and review the rendered pages before marking the draft ready.

The target workflow checks pull requests without deployment. After merge into
`main`, it checks and publishes only the static `site/` directory. No Hugo,
Node.js, Go, or Python package installation is needed.
