#!/usr/bin/env python3
# SPDX-FileCopyrightText: © 2026 Toon Verstraelen <Toon.Verstraelen@UGent.be>
# SPDX-License-Identifier: CC0-1.0

from stepup.core.api import mkdir, runsh, static

static("../../apptainer/", "../../apptainer/gpaw-cpu.sif")
mkdir("output")

CIDS = [
    "5000035",  # Quartz
    "1008189",  # Hydrogen peroxide
]
for cid in CIDS:
    runsh(
        f"curl https://www.crystallography.net/cod/{cid}.cif -o output/{cid}.cif",
        out=f"output/{cid}.cif",
    )
    runsh(
        "apptainer exec -e ../../../apptainer/gpaw-cpu.sif gpaw run "
        f"{cid}.cif --parameters xc=PBE,mode=fd",
        inp=f"{cid}.cif",
        out=f"{cid}.txt",
        workdir="output",
    )
