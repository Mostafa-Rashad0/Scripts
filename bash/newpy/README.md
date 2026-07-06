# newpy

A production-quality Bash CLI that scaffolds a modern Python project on Ubuntu — virtual environment, curated dev tooling, optional Git init, and starter files — in one command.

## Features

- Interactive project name prompt with validation (no invalid chars, no clobbering existing directories)
- Interactive project **path** prompt — choose exactly where the project folder is created (defaults to the current directory; supports relative paths, `~`, and offers to create the destination if it doesn't exist yet)
- Choice of **project type**: a standard layout (`src/`, `tests/`, `pyproject.toml`) or a **single-file script** (just `<project>.py`, nothing else)
- The entry script is named after the project itself (`<project>.py`), not `main.py`
- **Package setup**: install the default packages (with the option to layer custom packages on top), or specify a fully custom list instead — packages are validated against PyPI *before* installing (no failed-install attempts), with "did you mean...?" suggestions for typos
- **Editable default packages** — the default list lives in [`newpy-defaults.conf`](newpy-defaults.conf), a plain-text file next to the `newpy` script itself. Open it any time and add, remove, or version-pin packages; newpy reads it fresh on every run, so your changes apply to every project from then on. If the file is ever missing, newpy recreates it automatically with a small built-in fallback list.
- `requirements.txt` is always generated, regardless of your Git choice
- Optional Git initialization with a sensible Python `.gitignore` and an initial commit — `README.md` and `.gitignore` are only generated when Git is initialized
- **Auto-activation**: if the project is created in the same directory you ran `newpy` from, it drops you straight into a shell inside the project with the virtual environment already activated — no `cd`/`source` needed. If you pointed it at a different directory, it prints the exact `cd`/`source`/`python` commands instead.
- Colored, human-readable output; spinner while installing packages
- Execution logging to `~/.local/state/newpy/newpy.log`
- Graceful Ctrl+C handling and automatic cleanup on failure
- `--help` / `--version` flags

## Requirements

- Ubuntu 24.04+ (or similar)
- `python3` and the `venv` module (`sudo apt install python3-venv` if missing)
- Internet access (for PyPI package installs/validation)
- `git` (optional, only needed if you choose to initialize a repository)

## Installation

```bash
git clone https://github.com/Mostafa-Rashad0/newpy.git
cd newpy
chmod +x newpy
```

Optionally, put it on your `PATH`:

```bash
sudo cp newpy /usr/local/bin/newpy
sudo cp newpy-defaults.conf /usr/local/bin/newpy-defaults.conf
sudo chmod 644 /usr/local/bin/newpy-defaults.conf
```

> `/usr/local/bin` is owned by `root`, so once installed there:
> - `newpy-defaults.conf` needs to stay **readable by everyone** — `sudo chmod 644 ...` above ensures that, since newpy (running as your normal user) has to read it on every run.
> - **Editing** the installed copy afterward requires `sudo`, since it's now root-owned, e.g.:
>   ```bash
>   sudo nano /usr/local/bin/newpy-defaults.conf
>   ```
>   (or `sudo vim`, `sudo $EDITOR`, whichever you prefer). Writing to it without `sudo` will fail with a permissions error.
> - The `newpy-defaults.conf` file must always live in the same directory as the `newpy` script — wherever you move or install `newpy`, bring this file along with it.

## Customizing the default packages

Open [`newpy-defaults.conf`](newpy-defaults.conf) in any text editor:

```
# newpy default packages
#
# One package per line. Lines starting with '#' and blank lines
# are ignored. Edit this list to change what gets installed when
# you choose "Install default packages" in newpy.
# Version specifiers are fine, e.g.: requests>=2.31

requests
python-dotenv
rich
click
pytest
```

Add a package, remove one, or pin a version — save the file, and the very next time you run `newpy` the new list shows up in the package-setup prompt and gets installed. No need to edit the script itself.

If you installed `newpy` system-wide (into `/usr/local/bin`), remember the file there is owned by `root` — edit it with `sudo` (e.g. `sudo nano /usr/local/bin/newpy-defaults.conf`), or edit your local working copy and `sudo cp` it over again.

## Usage

```bash
newpy
```

Follow the prompts:

1. **Project name** and **path** (defaults to the current directory)
2. **Project type** — standard (`src/`, `tests/`, `pyproject.toml`) or single-file script
3. **Git** — yes/no (controls whether `README.md` and `.gitignore` are generated; `requirements.txt` is always generated either way)
4. **Packages** — install the defaults (with an option to add custom packages on top), or specify your own list instead

If the project was created in your current directory, newpy activates the virtual environment for you automatically. Otherwise, it prints the exact `cd`, `source`, and `python` commands to run.

```bash
newpy --help
newpy --version
```

## License

MIT — see [LICENSE](LICENSE).
