#!/usr/bin/env python3
"""
Retro Gaming Utilities CLI
A command-line interface for retro gaming utilities.
"""

from pathlib import Path

import click
from . import files


@click.group()
@click.version_option(version="0.1.0", prog_name="rgu")
def cli():
    """
    Retro Gaming Utilities (RGU) - A collection of tools for retro gaming enthusiasts.
    
    Use this tool to manage, fix, and enhance your retro gaming experience.
    """
    pass


@cli.command()
@click.option('--dry-run', is_flag=True, help='Do not rename files, just print what would be renamed')
@click.argument('path', type=click.Path(exists=True, file_okay=False, dir_okay=True))
def remove_num_index(path, dry_run):
    """
    Remove number index from file names

    Args:
        path: Path to the directory to remove number index from file names
    """
    files.remove_num_index_from_file_name(Path(path))


@ cli.command()
@click.option('--dry-run', is_flag=True, help='Do not remove files, just print what would be removed')
@click.argument('path', type=click.Path(exists=True, file_okay=False, dir_okay=True))
def remove_redundant_roms(path, dry_run):
    """
    Remove redundant ROMs from a directory

    Args:
        path: Path to the directory to remove redundant ROMs from
    """
    files.remove_redundant_roms(Path(path), dry_run)


def version():
    """Show version information."""
    click.echo("Retro Gaming Utilities v0.1.0")
    click.echo("Built with ❤️ for retro gaming enthusiasts")


if __name__ == '__main__':
    cli()
