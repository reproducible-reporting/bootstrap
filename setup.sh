#!/usr/bin/env bash
# SPDX-FileCopyrightText: © 2026 Toon Verstraelen <Toon.Verstraelen@UGent.be>
# SPDX-License-Identifier: CC0-1.0

# Settings
PYTHON_VERSION=3.14

# Bootstrap uv
mkdir -p .venv/bin/
curl -LsSf https://astral.sh/uv/install.sh | env UV_UNMANAGED_INSTALL=".venv/bin" sh

# Install venv in the same .venv directory
export UV_PYTHON_INSTALL_DIR=.venv/uv-python
.venv/bin/uv venv --allow-existing --python=$PYTHON_VERSION --managed-python

# Install dependencies
.venv/bin/uv sync

# Create the shell.sh script
cat > shell.sh << EOF
#!/usr/bin/env bash
export SOURCE_DATE_EPOCH=315532800
export PROJECT_ROOT=$PWD
source .venv/bin/activate
export STEPUP_PATH_FILTER='+../'
$SHELL -i
EOF
head -n-1 shell.sh | tail -n+2 > .envrc
chmod +x shell.sh

# Create the module file for HPC clusters (also works locally)
mkdir -p .venv/modules
cat > .venv/modules/bootstrap.lua << EOF
local project_root = "$PWD"
setenv("PROJECT_ROOT", project_root)
local venv = project_root .. "/.venv"
setenv("SOURCE_DATE_EPOCH", "315532800")
setenv("STEPUP_PATH_FILTER", "+../")
setenv("VIRTUAL_ENV", venv)
prepend_path("PYTHONPATH", venv .. "/lib/python$PYTHON_VERSION/site-packages")
prepend_path("PATH", venv .. "/bin")
EOF
