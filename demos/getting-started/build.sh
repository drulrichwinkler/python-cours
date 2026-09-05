#!/usr/bin/env bash
# Fixture for the "getting started" demo. The demo itself clones the repository,
# so this only clears what a previous take left behind.
set -euo pipefail
export PATH="$HOME/.docker/bin:$PATH"

BASE=/tmp/autodemo-start
REPO="$BASE/python-cours"

# Docker labels the container with the PHYSICAL path. On macOS /tmp is a symlink
# to /private/tmp, so filtering on the logical path silently matches nothing --
# the old container keeps running, keeps .venv mounted, and Docker's "deny delete"
# ACL then makes the clone impossible to remove.
REPO_PHYS=$(python3 -c 'import os,sys; print(os.path.realpath(sys.argv[1]))' "$REPO")

for folder in "$REPO" "$REPO_PHYS"; do
  ids=$(docker ps -aq --filter "label=devcontainer.local_folder=$folder" || true)
  [ -n "$ids" ] && echo "$ids" | xargs docker rm -f >/dev/null
done

# The mount point is released a moment after the container is gone.
sleep 1
rm -rf "$REPO"
echo "Fixture bereit: $BASE (Repo entfernt, die Demo klont selbst)"
