# Reliably Setup Action

A [GitHub Action](https://github.com/features/actions) for installing
[Reliably CLI](https://github.com/reliablyhq/cli) within your workflow,
so that the command is directly available in a job step.

You can use the Action as follows:

```yaml
name: Install Reliably CLI example
on: push
jobs:
  setup-reliably:
    runs-on: ubuntu-latest
    steps:
    - uses: reliablyhq/actions/setup@v1
```

The Reliably Setup Action has properties which are passed to the underlying script.
These are passed to the action using `with`.

| Property | Default | Description |
| --- | --- | --- |
| reliably-version | latest | Install a specific version of Reliably |

The Action also has outputs:

| Property | Default | Description |
| --- | --- | --- |
| version |   | The full version of the Reliably CLI installed |

For example, you can choose to install a specific version of Reliably.
The installed version can be grabbed from the output:

```yaml
name: Install Reliably CLI example with a specific version
on: push
jobs:
  setup-reliably:
    runs-on: ubuntu-latest
    steps:
    - uses: reliablyhq/actions/setup@v1
      id: reliably
      with:
        reliably-version: v0.1.0
    - name: Installed Reliably version
      run: echo "${{ steps.reliably.outputs.version }}"
```
