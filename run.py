#!/usr/bin/env python3
"""Entry point for the Paper-to-Notebook traditional server."""

import os
import subprocess
import sys

# Auto-activate the venv if we're not already running from it
VENV_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "venv")
VENV_PYTHON = os.path.join(VENV_DIR, "bin", "python3")

if os.path.exists(VENV_PYTHON) and sys.executable != VENV_PYTHON:
    # Re-launch this script with the venv Python
    os.execv(VENV_PYTHON, [VENV_PYTHON, __file__])

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
