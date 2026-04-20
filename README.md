<!--
SPDX-FileCopyrightText: © 2026 Toon Verstraelen <Toon.Verstraelen@UGent.be>
SPDX-License-Identifier: CC0-1.0
-->

![License](https://img.shields.io/github/license/reproducible-reporting/bootstrap)

# StepUp Bootstrap repository

This repository can be used as a template for one or more StepUp workflows.
You can simply fork or copy this repository to build your own workflows.

For basic usage, you only need a Linux environment with the `curl` command installed.
The `setup.sh` script will bootstrap a minimal self-contained Python environment and install StepUp and its dependencies.

If significant additional software is needed,
it is recommended to either use externally installed software,
or to work with Apptainer containers.
For the latter, you need to have `apptainer` installed on your system.
Some containers are provided in the sibling [container-factory](https://github.com/reproducible-reporting/container-factory) repository.

The minimal environment can be activated with a shell script (ideal for local hardware)
or with an LMod module file (better for HPC clusters).

## License

This repository is licensed under the [Creative Commons CC0-1.0 License](https://creativecommons.org/publicdomain/zero/1.0/).
This means that the files in this repository are in the public domain.
You can use them any way you like, without any restrictions or attribution requirements.
Feel free to assign a different license to your forked or copied repository if you wish.

## Getting started

Clone the repository (or fork it and clone your fork):

```bash
git clone git@github.com:reproducible-reporting/bootstrap.git
cd bootstrap
```

Create the Python environment with the `setup.sh` script:

```bash
./setup.sh
```

This will download and install [uv](https://docs.astral.sh/uv/)
and create a virtual environment in the `.venv` directory.

### Working in the StepUp environment

Before you can run `stepup boot` or use other packages,
it is recommended to activate the environment.

#### Using a subshell

A subshell is the simplest robust way to activate the environment.

```bash
./shell.sh
```

(This script is created by the `setup.sh` script.)
When you exit the subshell, you will return to your original environment.

The more traditional `source .venv/bin/activate` command is not recommended,
as it does not allow for customization.
In addition, exiting the shell offers a cleaner way to return to the original environment.

#### Using an LMod module

If you have LMod installed, e.g. on an HPC cluster, you can load the `bootstrap` module:

```bash
module use .venv/modules
module load bootstrap
```

This can be combined with other modules and does not require a subshell.

#### Example workflow

The [`workflows/matplotlib/`](workflows/matplotlib/) contains an example workflow that only needs the StepUp environment to run:

```bash
cd workflows/matplotlib/
stepup boot
```

### Adding more environment variables

If you need to add more environment variables, these need to be added to two files:

- `shell.sh`: for the subshell activation method
- `.venv/modules/bootstrap.lua`: for the LMod module

### Software management with uv

The Python environment is managed with [uv](https://docs.astral.sh/uv/),
which goes a lot further (at a higher speed) than the standard `pip` and `venv` tools.

A few useful commands:

```bash
uv add somepackage     # Add a new package to the environment
uv remove somepackage  # Remove a package from the environment
```

These commands will also update the `pyproject.toml` and `uv.lock` files,
which you can commit to Git.
This will get picked up when someone else runs the `setup.sh` script.
If you already ran the setup and someone else updated the `pyproject.toml` and `uv.lock` files,
you can sync the environment with the following command:

```bash
uv sync                # Sync the environment with the pyproject.toml and uv.lock files
```

The following commands are also useful:

```bash
uv lock --upgrade      # Upgrade all packages to their latest versions
uv run somecommand     # Run a command in the environment without activating it
```

For a complete list of features and commands,
see the [uv features](https://docs.astral.sh/uv/getting-started/features/).

## Working with Apptainer containers

This repository contains an example of an [Apptainer](https://apptainer.org/) definition to get you started.

### Building a container

We recommend that you pull only pre-built containers, with minimal modifications at most.
Apptainer is great for low-overhead execution of software.
Other tools, like podman or docker, are better suited for building and testing containers.
(See e.g. [container-factory](https://github.com/reproducible-reporting/container-factory) for examples of building containers with podman.)

See [`apptainer/`](apptainer/) for instructions on how to build and use the container.

### Using a container in a StepUp workflow

You can simply use StepUp's `runsh` command to run a command in a container.
For example, a minimal `plan.py` file like this will work:

```python
#!/usr/bin/env python3
from stepup.core.api import runsh, static

static("apptainer/", "apptainer/gpaw-cpu.sif")
runsh(
    "apptainer exec apptainer/gpaw-cpu.sif somecommand",
    inp=["apptainer/gpaw-cpu.sif", ...],
    out=[...],
)
```

The following two directories contain example workflows using containers:

- [`workflows/gpaw/`](workflows/gpaw/) runs a few small GPAW calculations on the local machine.
- [`workflows/slurm/`](workflows/slurm/) submits all calculations as Slurm jobs.
