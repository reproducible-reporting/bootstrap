<!--
SPDX-FileCopyrightText: © 2026 Toon Verstraelen <Toon.Verstraelen@UGent.be>
SPDX-License-Identifier: CC0-1.0
-->

# Apptainer example

Instructions:

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
