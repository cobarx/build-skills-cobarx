#!/usr/bin/env bash
#
# Stage the change in the agent's empty workspace, and run it once, as the developer says they did.
# The runner calls this with the workspace as the current directory, and only with --scaffold.

set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -R "$here/files/." .
python3 scripts/plot_signups.py data/signups.csv signups.png >/dev/null
