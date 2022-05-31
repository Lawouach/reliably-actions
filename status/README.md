# Reliably GitHub Action

Reliably integrates with GitHub as a [GitHub Action][gh-action] that you can add to your own GitHub CI/CD workflows.

[gh-action]: https://github.com/features/actions
[view-on-marketplace]: https://github.com/marketplace/actions/reliably-actions

You use the Reliably GitHub Action by including it in any of your GitHub workflow
YAML files:

```yaml
name: Example workflow using Reliably
on: push
jobs:
  reliably:
    runs-on: ubuntu-22.04
    steps:
      - uses: reliablyhq/actions/setup@v1
      - uses: reliablyhq/actions/status@v1
        env:
          RELIABLY_TOKEN: ${{ secrets.RELIABLY_TOKEN }}
          RELIABLY_ORG: ${{ secrets.RELIABLY_ORG }}
        with:
          selector: app=payment
```

The code above adds a new job called `reliably`. This job tells reliably 
to fetch the status of objectives matching the given selector and
output to stdout as a JSON payload.

The Reliably GitHub Action has properties which are passed to the underlying image.
These are passed to the action using `with`.

| Property | Description |
| --- | --- |
| selector | Comma seperate k=v pairs of labels of your objectives/scorecards |
| kind | The kind of resources to scope the selectors to: objective, score, scorecard |
| format | The format of the status output: json, yaml or text |

## Getting your Reliably token

The Action example above refer to a Reliably access token:

```yaml
env:
  RELIABLY_TOKEN: ${{ secrets.RELIABLY_TOKEN }}
```

You can retrieve your access token once authenticated with the CLI:

```console
reliably auth status --show-token
```