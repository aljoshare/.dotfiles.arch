#!/usr/bin/env python3
"""Sync dotfiles from $HOME into this repository."""

import argparse
import shutil
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml")
    raise SystemExit(1)

REPO_ROOT = Path(__file__).resolve().parent
CONFIG = REPO_ROOT / "sync.yaml"


def load_paths() -> list[str]:
    with open(CONFIG) as f:
        data = yaml.safe_load(f)
    return data["paths"]


def sync(dry_run: bool = False) -> None:
    home = Path.home()
    paths = load_paths()

    for rel in paths:
        src = home / rel
        dest = REPO_ROOT / rel

        if not src.exists():
            print(f"  SKIP  {rel} (source not found)")
            continue

        if dry_run:
            print(f"  WOULD {rel}")
            continue

        if src.is_dir():
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(src, dest, dirs_exist_ok=True)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)

        print(f"  OK    {rel}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync dotfiles from $HOME into repo")
    parser.add_argument(
        "--dry-run", action="store_true", help="Preview without copying"
    )
    args = parser.parse_args()

    print("Syncing dotfiles..." if not args.dry_run else "Dry run:")
    sync(dry_run=args.dry_run)
    print("Done.")


if __name__ == "__main__":
    main()
