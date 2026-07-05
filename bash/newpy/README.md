# newpy

A production-quality Bash CLI that scaffolds a modern Python project on Ubuntu — virtual environment, curated dev tooling, optional Git init, and starter files — in one command.

## Features

- Interactive project name prompt with validation (no invalid chars, no clobbering existing directories)
- Interactive project **path** prompt — choose exactly where the project folder is created (defaults to the current directory; supports relative paths, `~`, and offers to create the destination if it doesn't exist yet)
- Choice of **project type**: a standard layout (`src/`, `tests/`, `pyproject.toml`) or a **single-file script** (just `<project>.py`, nothing else)
- The entry script is named after the project itself (`<project>.py`), not `main.py`
- Choice of **package setup**: install a curated set of 5 default packages (`requests`, `python-dotenv`, `rich`, `click`, `pytest`) or specify your own — packages are validated against PyPI *before* installing (no failed-install attempts), with "did you mean...?" suggestions for typos
- Optional Git initialization with a sensible Python `.gitignore` and an initial commit — `README.md`, `requirements.txt`, and `.gitignore` are only generated when Git is initialized
- Colored, human-readable output; spinner while installing packages
- Execution logging to `~/.local/state/newpy/newpy.log`
- Graceful Ctrl+C handling and automatic cleanup on failure
- `--help` / `--version` flags

## Requirements

- Ubuntu 24.04+ (or similar) or any linux distribution 
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
```

## Usage

```bash
newpy
```

Follow the prompts:

1. **Project name** and **path** (defaults to the current directory)
2. **Project type** — standard (`src/`, `tests/`, `pyproject.toml`) or single-file script
3. **Git** — yes/no (controls whether `README.md`, `requirements.txt`, and `.gitignore` are generated)
4. **Packages** — install the 5 defaults, or specify your own

When it finishes, it prints the exact commands to `cd` into your new project, activate the virtual environment, and run the script — it never changes your shell's directory for you.

```bash
newpy --help
newpy --version
```

## License

MIT — see [LICENSE](LICENSE).
