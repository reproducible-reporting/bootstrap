#!/usr/bin/env python3
# SPDX-FileCopyrightText: © 2026 Toon Verstraelen <Toon.Verstraelen@UGent.be>
# SPDX-License-Identifier: CC0-1.0

import matplotlib.pyplot as plt

with open("output/fib.txt") as f:
    data = [int(line.strip()) for line in f]

fig, ax = plt.subplots()
ax.plot(data, marker="o", linestyle="none")
ax.set_xlabel("Index")
ax.set_ylabel("Value")
ax.set_title("Fibonacci Sequence")
plt.savefig("output/plot.png")
