#!/usr/bin/env python3
# SPDX-FileCopyrightText: © 2026 Toon Verstraelen <Toon.Verstraelen@UGent.be>
# SPDX-License-Identifier: CC0-1.0

from stepup.core.api import copy, mkdir, runsh, static
from stepup.queue.api import sbatch

static("../../apptainer/", "../../apptainer/gpaw-cpu.sif", "static/", "static/slurmjob.sh")
mkdir("output")


def plan_gpaw_job(cid):
    mkdir(f"output/{cid}")
    runsh(
        f"curl https://www.crystallography.net/cod/{cid}.cif -o output/{cid}/structure.cif",
        out=f"output/{cid}/structure.cif",
    )
    copy("static/slurmjob.sh", f"output/{cid}/slurmjob.sh")
    sbatch(
        f"output/{cid}/",
        inp=["structure.cif", "../../../../apptainer/gpaw-cpu.sif"],
        out="structure.txt",
    )


plan_gpaw_job("5000035")  # Quartz
plan_gpaw_job("1008189")  # Hydrogen peroxide
