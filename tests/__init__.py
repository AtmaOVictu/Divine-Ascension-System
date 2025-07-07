import os
import sys

# Append the repository root to sys.path so tests can import divine_agents
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
