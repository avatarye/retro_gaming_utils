# Retro Gaming Utilities (RGU)

A command-line interface for retro gaming enthusiasts to manage, fix, and enhance their retro gaming experience.

## Features

- **Fix Command**: Automatically fix common issues with retro gaming files
- **Analyze Command**: Generate detailed reports about your retro gaming collection
- **Version Command**: Display version information

## Installation

### Development Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd retro_gaming_utils
```

2. Install in development mode:
```bash
pip install -e .
```

### Production Installation

```bash
pip install .
```

## Usage

After installation, you can use the `rgu` command:

### Basic Commands

```bash
# Show help
rgu --help

# Show version
rgu version

# Show help for a specific command
rgu fix --help
rgu analyze --help
```

### Fix Command

The `fix` command helps resolve common issues with retro gaming files:

```bash
# Fix a single file
rgu fix /path/to/game.rom

# Fix all files in a directory
rgu fix /path/to/roms/

# Dry run mode (show what would be fixed without making changes)
rgu fix --dry-run /path/to/roms/

# Verbose output
rgu fix -v /path/to/roms/
```

### Analyze Command

The `analyze` command provides detailed information about your retro gaming files:

```bash
# Analyze a single file
rgu analyze /path/to/game.rom

# Analyze a directory
rgu analyze /path/to/roms/

# Output in different formats
rgu analyze --format json /path/to/roms/
rgu analyze --format yaml /path/to/roms/
rgu analyze --format text /path/to/roms/  # default
```

## Development

### Project Structure

```
src/
├── retro_gaming_utilities/
│   ├── __init__.py      # Package initialization
│   ├── cli.py          # CLI entry point and commands
│   └── files.py        # File operations and utilities
├── pyproject.toml      # Project configuration
└── README.md           # This file
```

### Testing

Run the test script to verify the CLI works:

```bash
python test_cli.py
```

### Adding New Commands

To add new commands, edit `cli.py` and add new functions decorated with `@cli.command()`.

### Extending File Operations

Modify the functions in `files.py` to add real retro gaming file validation and fixing logic.

## Dependencies

- **Click**: CLI framework
- **Rich**: Enhanced terminal output (planned for future use)

## License

[Your License Here]
