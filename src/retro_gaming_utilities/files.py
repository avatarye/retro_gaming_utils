"""
Retro Gaming Utilities - File Operations Module

This module provides functions for fixing and analyzing retro gaming files.
"""

from collections import defaultdict

from pathlib import Path
from typing import Union, Dict, Any, List


def remove_num_index_from_file_name(dir: Path, dry_run: bool = True) -> bool:
    dir = Path(dir)
    files_to_rename = []
    good_to_go = False
    for file in dir.iterdir():
        if file.is_file():
            segs = file.stem.split(' ')
            if not (len(segs) and segs[0].isdigit()):
                segs = file.stem.split('.')
                if len(segs) > 1 and segs[0].isdigit():
                    good_to_go = True
            else:
                good_to_go = True

            if good_to_go:
                new_name = (' '.join(segs[1:]).strip(' -')) + file.suffix
                new_name = file.parent / new_name
                files_to_rename.append((file, new_name))

    if len(files_to_rename) > 0:
        for file, new_name in files_to_rename:
            if new_name.exists():
                print(f"File {new_name} already exists")
            else:
                if not dry_run:
                    file.rename(new_name)
                    print(f"Renamed {file} to {new_name}")
                else:
                    print(f"Would rename {file} to {new_name}")
    return True


def remove_redundant_roms(dir: Path, dry_run: bool = True) -> bool:

    dir = Path(dir)
    files_to_remove = []
    file_types_to_preserve = ('.zip', '.7z', '.rar', '.tar', '.gz', '.bz2', '.xz')

    for file_type in file_types_to_preserve:
        files_to_check = [file for file in dir.iterdir() if file.is_file() and file.suffix.lower() == file_type]
        for file in files_to_check:
            uncompressed_file = file.with_suffix('.bin')
            if uncompressed_file.exists():
                files_to_remove.append(uncompressed_file)

    for file in files_to_remove:
        if not dry_run:
            file.unlink()
            print(f"Removing {file}")
        else:
            print(f"Would remove {file}")

    return True