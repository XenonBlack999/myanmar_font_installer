# myanmar_font_installer
# Linux Myanmar Font Installer

## Overview
This script automatically installs all `.ttf` font files found in the current directory to the appropriate font directory on a Linux system. It also refreshes the font cache to make the newly installed fonts available for use.

## Features
- Scans the current directory for `.ttf` font files.
- Installs fonts to the user or system-wide font directory.
- Refreshes the font cache after installation.
- No manual font selection required.

## Prerequisites
- Python 3
- Linux OS
- `fc-cache` installed (part of `fontconfig` package)

## Installation & Usage
Cloning from github 
```https://github.com/XenonBlack999/myanmar_font_installer.git```

```cd myanmar_font_installer```

### User-Level Installation
Installs fonts to `~/.local/share/fonts/` (no root permissions required):
```sh
python install_font.py
```

### System-Wide Installation
Installs fonts to `/usr/share/fonts/` (requires root permissions):
```sh
sudo python install_font.py --system
```

## Notes
- Ensure the script is executed in the same directory as the `.ttf` font files.
- If fonts do not appear after installation, try restarting your application or session.

