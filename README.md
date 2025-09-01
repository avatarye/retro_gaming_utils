# Retro Gaming Utilities (RGU)

A command-line interface for retro gaming enthusiasts to manage, fix, and enhance their retro gaming experience.

## Features

- **Remove Number Index**: Remove number prefixes from ROM file names
- **Remove Redundant ROMs**: Remove uncompressed ROM files when compressed versions exist
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
rgu --version

# Show help for a specific command
rgu remove-num-index --help
rgu remove-redundant-roms --help
```

### Remove Number Index Command

The `remove-num-index` command removes number prefixes from ROM file names:

```bash
# Remove number index from files in a directory
rgu remove-num-index /path/to/roms/

# Dry run mode (show what would be renamed without making changes)
rgu remove-num-index --dry-run /path/to/roms/
```

### Remove Redundant ROMs Command

The `remove-redundant-roms` command removes uncompressed ROM files when compressed versions exist:

```bash
# Remove redundant ROM files in a directory
rgu remove-redundant-roms /path/to/roms/

# Dry run mode (show what would be removed without making changes)
rgu remove-redundant-roms --dry-run /path/to/roms/
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

### Adding New Commands

To add new commands, edit `cli.py` and add new functions decorated with `@cli.command()`.

### Extending File Operations

The `files.py` module contains the core functionality:
- `remove_num_index_from_file_name()`: Removes number prefixes from file names
- `remove_redundant_roms()`: Removes uncompressed ROMs when compressed versions exist

## Dependencies

- **Click**: CLI framework (>=8.2.1)
- **Rich**: Enhanced terminal output (>=14.1.0)

## License

[Your License Here]
