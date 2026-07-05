# newpy

A production-quality Bash CLI that scaffolds a modern Python project on Ubuntu — virtual environment, curated dev tooling, optional Git init, and starter files — in one command.

## Features

- Interactive project name prompt with validation (no invalid chars, no clobbering existing directories)
- Interactive project **path** prompt — choose exactly where the project folder is created (defaults to the current directory; supports relative paths, `~`, and offers to create the destination if it doesn't exist yet)
- Creates `.venv`, upgrades pip, installs a curated default toolchain:
  `black`, `ruff`, `pytest`, `isort`, `mypy`, `rich`, `python-dotenv`
- Optional extra packages, validated against PyPI *before* installing (no failed-install attempts), with "did you mean...?" suggestions for typos
- Optional Git initialization with a sensible Python `.gitignore` and an initial commit
- Generates `README.md`, `pyproject.toml` (Black/Ruff/isort configured), and a starter `main.py`
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

Follow the prompts. When it finishes, it prints the exact commands to `cd` into your new project and activate the virtual environment — it never changes your shell's directory for you.

```bash
newpy --help
newpy --version
```

## License

MIT — see [LICENSE](LICENSE).
