# Reliably GitHub Action

Reliably integrates with GitHub as a [GitHub Action][gh-action] that you can add to your own GitHub CI/CD workflows. Our Action is available on GitHub's [Marketplace][view-on-marketplace].

[gh-action]: https://github.com/features/actions
[view-on-marketplace]: https://github.com/marketplace/actions/reliably-github-action

## Available actions

This repository contains a set of GitHub actions for using Reliably
within your workflows:

- [Setup](setup): Install Reliably CLI directly in your workflow runner
- [Scan](scan): Scan your source code for suggestions
- [SLO Report](slo-report): Generate your SLO report

## Generic action

The following action allows any user to use the CLI as a GitHub action:

```yaml
uses: reliablyhq/actions@v1
env:
  RELIABLY_TOKEN: ${{ secrets.RELIABLY_TOKEN }}
continue-on-error: true
with:
  args: --help
```

## Getting your Reliably token

Most of our actions required a valid Reliably access token for making calls
to our API. You can define the environment for a step, job, or entire workflow:

```yaml
env:
  RELIABLY_TOKEN: ${{ secrets.RELIABLY_TOKEN }}
```

You can retrieve your access token once authenticated with the CLI:
```
$ reliably auth status --show-token
```
