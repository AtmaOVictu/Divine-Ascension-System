import random
from typing import List


class MetaAgent:
    """Generate random tests based on unused data."""

    def __init__(self, name: str, known_data: List[str] | None = None) -> None:
        self.name = name
        self.known_data = known_data or [
            "Test1",
            "Test2",
            "Test3",
            "Test4",
            "Test5",
        ]
        self.test_results: List[str] = []

    def generate_random_test(self) -> str:
        """Generate a random test from untested data."""
        unused = [d for d in self.known_data if d not in self.test_results]
        if not unused:
            return "Vsi testi so že bili izvedeni."
        test = random.choice(unused)
        self.test_results.append(test)
        return f"Meta test: {test} (Preizkušen)"

    def execute_test(self) -> str:
        """Execute a randomly generated test."""
        return self.generate_random_test()

    def get_test_results(self) -> List[str]:
        """Return the list of executed tests."""
        return self.test_results


class RandomCodeTester:
    """Select and test random code blocks once."""

    def __init__(self, blocks: List[str]):
        self.blocks = blocks
        self.tested_blocks: List[str] = []

    def select_random_block(self) -> str:
        """Select a random block that has not been tested yet."""
        unused = [b for b in self.blocks if b not in self.tested_blocks]
        if not unused:
            return "Vsi bloki so že bili preizkušeni."
        block = random.choice(unused)
        self.tested_blocks.append(block)
        return f"Preizkušen blok: {block}"

    def test_random_block(self) -> str:
        """Execute a randomly selected block."""
        return self.select_random_block()

    def get_tested_blocks(self) -> List[str]:
        """Return all tested blocks."""
        return self.tested_blocks
