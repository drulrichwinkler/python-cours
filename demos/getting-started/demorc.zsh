# Docker Desktop puts its binaries here and only patches the login shell's PATH.
# The demo runs in a freshly generated zsh, so it has to be added explicitly --
# otherwise `devcontainer up` fails with "spawn docker ENOENT".
export PATH="$HOME/.docker/bin:$PATH"

# Docker Desktop appends a "What's next: Try Docker Debug ..." advert to every
# command. In a teaching recording it appears after each step and pushes the
# real output off the screen.
export DOCKER_CLI_HINTS=false
