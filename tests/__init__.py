import os
import sys

# Ensure repository root is on the path when running tests via `pytest`.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
