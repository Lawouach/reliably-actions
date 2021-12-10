# Reliably GitHub Actions

Reliably integrates with GitHub as a [GitHub Action][gh-action] that you can add to your own GitHub CI/CD workflows. Our Actions are available on GitHub's [Marketplace][view-on-marketplace].

[gh-action]: https://github.com/features/actions
[view-on-marketplace]: https://github.com/marketplace/actions/reliably-actions

## Available actions

This repository contains a set of GitHub actions for using Reliably
within your workflows:

- [Setup](setup): Install Reliably CLI directly in your workflow runner
- [Scan](scan): Scan your source code for suggestions
- [SLO Report](slo-report): Generate your SLO report
- [Create An Operation](operation): Inform Reliably about an operation that has happened in your pipeline.

## Generic action

The following action allows users to use the CLI directly as a GitHub action:

```yaml
uses: reliablyhq/actions@v1
with:
  args: --help
```

Arguments to the CLI can be passed using the `with.args` syntax. [See the doc](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idstepswithargs).

## Getting your Reliably token

Most of our actions required a valid Reliably access token for making calls
to our API. You can define the environment for a step, job, or entire workflow:

```yaml
env:
  RELIABLY_TOKEN: ${{ secrets.RELIABLY_TOKEN }}
```

You can retrieve your access token once authenticated with the CLI:

```console
reliably auth status --show-token
```
