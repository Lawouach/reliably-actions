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
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: reliablyhq/actions/operation@v1
        env:
          RELIABLY_TOKEN: ${{ secrets.RELIABLY_TOKEN }}
          RELIABLY_ORG: ${{ secrets.RELIABLY_ORG }}
        with:
          service: my awesome service
          type: build
          outcome: success
```

The code above adds a new job called `reliably`. This job tells reliably that an operation has occured on a particular service, and the outcome of that operation.

The Reliably GitHub Action has properties which are passed to the underlying image.
These are passed to the action using `with`.

| Property | Description |
| --- | --- |
| service | The name of the service this applies to |
| type | The type of operation being performed (i.e. build, deployment, etc.) |
| outcome | The outcome of the operation (success, fail, unknown, etc.) |

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