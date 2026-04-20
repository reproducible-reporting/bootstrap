<!--
SPDX-FileCopyrightText: © 2026 Toon Verstraelen <Toon.Verstraelen@UGent.be>
SPDX-License-Identifier: CC0-1.0
-->

# Apptainer example

Note that all the instructions below only rely on apptainer.
They work without StepUp.

## Container build instructions

1. Determine the x86-64 architecture level of your host operating system:

   ```bash
   /lib64/ld-linux-x86-64.so.2 --help | grep -E "v[234]"
   ```

   You will get an output like this:

   ```
   x86-64-v4
   x86-64-v3 (supported, searched)
   x86-64-v2 (supported, searched)
   ```

   This means that `x86-64-v3` is the highest architecture level supported by your host operating system.

1. Build the Apptainer image using the appropriate architecture level:

   ```bash
   apptainer build --build-arg x86_64_level=v3 gpaw-cpu.sif gpaw-cpu.def
   ```

## Basic test

You can test your container with the following command:

```bash
apptainer exec gpaw-cpu.sif gpaw test
```

## Interactive use

To work interactively with a container, you can launch a subshell as follows:

```bash
apptainer run gpaw-cpu.sif
```

In the container, you can test GPAW as follows:

```bash
gpaw test
```
