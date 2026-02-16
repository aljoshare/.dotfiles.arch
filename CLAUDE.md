# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal dotfiles for an Arch Linux + Hyprland (Wayland) desktop environment. Configurations are tracked directly in the repo with their dotfile paths preserved (no stow or symlink manager). There are no install/setup scripts — files are deployed manually.

## Key Commands

```bash
# Secret scanning (pre-commit hook)
pre-commit run --all-files
pre-commit install            # activate git hooks locally

# TruffleHog directly
trufflehog git file://. --since-commit HEAD --results=verified,unknown --fail --no-update
```

There is no build system, linter, or test suite.

## Commit Conventions

Conventional commits with optional scope: `feat(hypr):`, `fix(waybar):`, `ci:`, `chore:`, `docs:`. Feature branches use `feat/`, `fix/`, `ci/` prefixes and merge to `main` via PRs.

## Architecture

- **Desktop stack:** Hyprland compositor → Waybar (status bar) → Wofi (launcher) → Hyprpaper (wallpaper) → Hyprlock (lock screen) → Greetd/tuigreet (login)
- **Terminal stack:** Alacritty → Zsh (Oh-My-Zsh) → Zellij (multiplexer with custom layouts)
- **Theme:** Catppuccin Mocha applied consistently across all components; Gruvbox as alternate
- **Keyboard layout:** German (de)
- **Editor:** Zed with vi mode, prettier for formatting
- **Zellij layouts:** `default.kdl` (dev), `info.kdl` (newsboat/weather/gh-dash), `recon.kdl` (security tools)
- **`.paclist`:** Canonical list of Arch packages (129 entries) — update this when adding/removing system packages

## Security

Secrets detection is enforced via TruffleHog both in CI (`.github/workflows/secrets-detection.yml`) and as a pre-commit/pre-push hook. Gitleaks config exists at `.gitleaks.toml`.
