#!/usr/bin/env bash
#
# Stage the change in the agent's empty workspace.
# The runner calls this with the workspace as the current directory, and only with --scaffold.

set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -R "$here/files/." .
