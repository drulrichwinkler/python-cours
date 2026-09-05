# Demo: getting started

Source for the recorded walkthrough — clone, container, the three checks, and
exercise 00 solved. Author material, not part of the course itself.

Recorded with `autodemo`, a local tool: a driver types the script into a tmux
session character by character while asciinema records.

## Recording it again

```bash
cd demos/getting-started
./build.sh                       # clears the previous take
DEMO_RC=$PWD/demorc.zsh \
  ~/work/vorlesungen/iot/autodemo.sh demo.txt python-course-start --gif --voice
```

`build.sh` only removes leftovers. The demo clones the repository itself, from
GitHub, so what you see is what a student gets.

## Four things that broke, and why they are in these files

Every one of them produced a recording that looked plausible and was wrong.
They are written down so the next take does not rediscover them.

**`demorc.zsh` sets `PATH`.** The demo runs in a freshly generated zsh that never
sourced a login profile, so Docker Desktop's `~/.docker/bin` is missing and
`devcontainer up` dies with `spawn docker ENOENT`. Everything after that section
was dead in take 1.

**`demorc.zsh` sets `DOCKER_CLI_HINTS=false`.** Docker appends a three-line
advert — "What's next: Try Docker Debug …" — to *every* command. In take 2 it
appeared eight times and pushed the real output off the screen.

**`build.sh` resolves the physical path.** Docker labels a container with the
real path, and on macOS `/tmp` is a symlink to `/private/tmp`. Filtering on the
logical path matches nothing: the old container keeps running, keeps `.venv`
mounted, and Docker's `deny delete` ACL then makes the clone impossible to
remove.

**`demo.txt` searches for `TODO`, not for `return 0.0`.** The latter appears
twice in `exercise_01.py` — once in the docstring, once in the code. The editor
jumped to the first hit and cut up the task description instead of the code.

## Checking a take

```bash
python3 ~/work/vorlesungen/iot/pruef_cast.py /tmp/python-course-start-*.cast demo.txt
git -C /tmp/autodemo-start/python-cours diff --stat   # must be 1 insertion, 1 deletion
```

And read the `Zeitbasis:` line in the recorder's output. It should confirm nearly
every voiced line — "1 of 22" means the audio is misplaced across the whole
recording, not that one sentence slipped.
