import sys
from pathlib import Path

# Ensure package root is on PYTHONPATH for pytest execution
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
