import sys
from pathlib import Path

# Ensure the parent directory is on the path so tests can import the package
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
