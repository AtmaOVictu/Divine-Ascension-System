import random
from typing import List, Dict, Tuple


class LearningTestLoop:
    """Iterate over test versions and learn from their results."""

    def __init__(self, versions: List[str]):
        self.versions = versions
        self.results: Dict[str, float] = {}

    def run_test(self, version: str) -> str:
        """Simulate running a test version and store its success rate."""
        success_rate = random.uniform(0, 1)
        self.results[version] = success_rate
        return "Pass" if success_rate > 0.5 else "Fail"

    def evaluate(self) -> Tuple[str, float]:
        """Return the best performing test version and its score."""
        best_version = max(self.results, key=self.results.get)
        return best_version, self.results[best_version]

    def loop(self, iterations: int = 3) -> None:
        """Run the learning loop for the specified iterations."""
        for _ in range(iterations):
            for version in list(self.versions):
                self.run_test(version)
            best_version, _ = self.evaluate()
            self.versions.append(f"{best_version}_improved")
