#!/usr/bin/env python3
"""Entry-point wrapper for the demonstration runner."""

import sys
from pathlib import Path

# Ensure package root is on path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.demo_run import main

if __name__ == "__main__":
    main()
