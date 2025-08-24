"""
Retro Gaming Utilities Package

A collection of tools for retro gaming enthusiasts.
"""

from .cli import cli
from .files import remove_num_index_from_file_name

__version__ = "0.1.0"
__all__ = ["cli", "remove_num_index_from_file_name"]
