"""Utility functions for repository metrics."""
from pathlib import Path
import subprocess


def count_python_lines() -> int:
    """Return total number of lines across tracked Python files.

    Files are gathered from the current Git HEAD using ``git ls-files``.
    """
    result = subprocess.run(
        ["git", "ls-files", "*.py"],
        stdout=subprocess.PIPE,
        text=True,
        check=True,
    )
    files = [Path(f) for f in result.stdout.splitlines() if f]
    total = 0
    for path in files:
        with path.open("r", encoding="utf-8") as fh:
            total += sum(1 for _ in fh)
    return total
