#!/usr/bin/env python3
# SPDX-FileCopyrightText: © 2026 Toon Verstraelen <Toon.Verstraelen@UGent.be>
# SPDX-License-Identifier: CC0-1.0

from stepup.core.api import mkdir, runsh, static

static("generate.py", "plot.py")
mkdir("output")
runsh("./generate.py > output/fib.txt", inp=["generate.py"], out=["output/fib.txt"])
runsh("./plot.py", inp=["plot.py", "output/fib.txt"], out=["output/plot.png"])
