"""Test package initialization."""

import os
import sys

# Ensure project root is on sys.path for imports
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Optional hooks for pytest

def setup_module(module):
    print("Setting up test environment...")


def teardown_module(module):
    print("Cleaning up after tests...")
