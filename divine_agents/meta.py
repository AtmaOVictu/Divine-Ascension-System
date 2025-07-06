import random
from typing import List

class MetaAgent:
    """Meta agent capable of generating random tests based on known data."""

    def __init__(self, name: str, known_data: List[str] | None = None) -> None:
        self.name = name
        self.test_results: List[str] = []
        self.known_data = known_data or [
            "Test1",
            "Test2",
            "Test3",
            "Test4",
            "Test5",
        ]

    def generate_random_test(self) -> str:
        """Return a random unused test and mark it as used."""
        unused = [data for data in self.known_data if data not in self.test_results]
        if not unused:
            return "Vsi testi so že bili izvedeni"
        choice = random.choice(unused)
        self.test_results.append(choice)
        return f"Meta test: {choice} (Preizkušen)"

    def execute_test(self) -> str:
        """Execute and return the result of a generated test."""
        return self.generate_random_test()

    def get_test_results(self) -> List[str]:
        """Return the list of executed tests."""
        return self.test_results


class RandomCodeTester:
    """Randomly select code blocks for testing without repetition."""

    def __init__(self, blocks: List[str]):
        self.blocks = blocks
        self.tested_blocks: List[str] = []

    def select_random_block(self) -> str:
        """Select an unused block for testing."""
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
        """Return list of tested blocks."""
        return self.tested_blocks
