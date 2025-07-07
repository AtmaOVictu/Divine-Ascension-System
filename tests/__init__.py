import os
import sys

# Ensure package root is on the path when running `pytest`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
