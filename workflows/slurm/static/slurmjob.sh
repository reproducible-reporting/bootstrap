#!/usr/bin/env bash
# SPDX-FileCopyrightText: © 2026 Toon Verstraelen <Toon.Verstraelen@UGent.be>
# SPDX-License-Identifier: CC0-1.0
#SBATCH --job-name=gpaw
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --time=00:30:00
#SBATCH --mem=7G

apptainer exec ../../../../apptainer/gpaw-cpu.sif \
  mpiexec -n 2 gpaw run structure.cif --parameters xc=PBE,mode=fd
