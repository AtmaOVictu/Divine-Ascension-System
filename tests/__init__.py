import os
import sys

# Ensure parent directory is on the import path so tests can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
