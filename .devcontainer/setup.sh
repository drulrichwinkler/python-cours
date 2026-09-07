#!/usr/bin/env bash
# Runs once, after the container is created.
#
# Verified on 2026-09-05 with Docker 29.1.3 and @devcontainers/cli:
# container builds, this script completes, and inside it mypy, ruff and all
# three notebooks pass. Python in the image was 3.12.11.
#
# Everything the course needs is installed here, so a fresh container is ready
# to work in: no "pip install", no manual virtual environment.
set -euo pipefail

echo "==> Claiming the .venv volume"
# The named volume from devcontainer.json is mounted as root. Hand it to the
# user we actually work as, otherwise uv cannot write into it.
sudo chown -R "$(id -u):$(id -g)" .venv

echo "==> Installing uv"
# Astral's documented install method. It needs curl, which the base image has.
curl -LsSf https://astral.sh/uv/install.sh | sh

# The installer puts uv in ~/.local/bin. Make it available now and in every
# future shell in this container.
export PATH="$HOME/.local/bin:$PATH"
grep -qxF 'export PATH="$HOME/.local/bin:$PATH"' "$HOME/.bashrc" \
  || echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"

echo "==> Installing the course environment"
# --locked refuses to silently update uv.lock: everyone gets identical versions.
# This installs everything the course needs, including the packages for Part 5 --
# one setup, and nothing to install again at module 16.
uv sync --locked

echo "==> Checking that it works"
uv run python --version
uv run pytest -m "not your_turn" -q

cat <<'MSG'

  Ready.

  Start here:   00_setup/README.md
  Open the tour: uv run jupyter lab 00_setup/explore.ipynb

  The three checks:
    uv run pytest 00_setup     does it compute the right thing?
    uv run mypy                do the types line up?
    uv run ruff check .        is the style clean?

MSG
