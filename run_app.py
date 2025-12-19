# run_app.py
"""
EXE-safe entry point for Data Explorer Dashboard.
This avoids relative-import issues in PyInstaller.
"""

import sys
import os

# Ensure project root is on sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from app.main import main

if __name__ == "__main__":
    main()