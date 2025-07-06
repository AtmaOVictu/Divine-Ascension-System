"""Meta testing utilities for dynamic agent testing."""

from __future__ import annotations

import random
from typing import List, Optional


class MetaAgent:
    """Agent that generates and tracks random tests based on known data."""

    def __init__(self, name: str, known_tests: Optional[List[str]] = None) -> None:
        self.name = name
        self.test_results: List[str] = []
        self.known_tests = known_tests or [
            "Test1",
            "Test2",
            "Test3",
            "Test4",
            "Test5",
        ]

    def generate_random_test(self) -> Optional[str]:
        """Return a random unused test identifier or ``None`` if exhausted."""
        unused = [t for t in self.known_tests if t not in self.test_results]
        if not unused:
            return None
        test = random.choice(unused)
        self.test_results.append(test)
        return f"Meta test: {test} (Preizščen)"

    def execute_test(self) -> Optional[str]:
        """Execute a single randomly selected test."""
        return self.generate_random_test()

    def get_test_results(self) -> List[str]:
        """Return a list of completed tests."""
        return self.test_results


class RandomCodeTester:
    """Utility that randomly selects code blocks for execution."""

    def __init__(self, blocks: List[str]):
        self.blocks = blocks
        self.tested_blocks: List[str] = []

    def select_random_block(self) -> Optional[str]:
        """Return a random untested block or ``None`` if all tested."""
        unused = [b for b in self.blocks if b not in self.tested_blocks]
        if not unused:
            return None
        block = random.choice(unused)
        self.tested_blocks.append(block)
        return f"Preizščen blok: {block}"

    def test_random_block(self) -> Optional[str]:
        """Execute a randomly selected code block."""
        return self.select_random_block()

    def get_tested_blocks(self) -> List[str]:
        """Return the list of already tested blocks."""
        return self.tested_blocks
