#!/usr/bin/env python3
# SPDX-FileCopyrightText: © 2026 Toon Verstraelen <Toon.Verstraelen@UGent.be>
# SPDX-License-Identifier: CC0-1.0

a0 = 1
a1 = 1
print(a0)
print(a1)
for _ in range(10):
    tmp = a0 + a1
    print(tmp)
    a0 = a1
    a1 = tmp
