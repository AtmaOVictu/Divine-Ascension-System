import os
import sys

# Ensure project root is in sys.path for test imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def setup_module(module):
    """Setup actions run before any tests in the package."""
    print("Initializing test environment...")


def teardown_module(module):
    """Cleanup actions run after all tests in the package."""
    print("Cleaning up test environment...")
