#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:14:59 2025

@author: xenonblack
"""
import os
import sys
import shutil
import subprocess
        

FONT_DIR_SYSTEM = "/usr/share/fonts"
FONT_DIR_USER = os.path.expanduser("~/.local/share/fonts")

def install_fonts(system_wide=False):
    """Installs all .ttf fonts found in the current directory."""
    target_dir = FONT_DIR_SYSTEM if system_wide and os.geteuid() == 0 else FONT_DIR_USER
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
    
    font_files = [f for f in os.listdir('.') if f.lower().endswith('.ttf')]
    if not font_files:
        print("No .ttf font files found in the current directory.")
        sys.exit(1)
    
    for font_file in font_files:
        target_path = os.path.join(target_dir, font_file)
        shutil.copy(font_file, target_path)
        print(f"Installed '{font_file}' to '{target_dir}'")
    
    subprocess.run(["fc-cache", "-f", "-v"])
    print("Font cache updated.")

if __name__ == "__main__":
    system_wide = "--system" in sys.argv
    install_fonts(system_wide)
