import random
from typing import Dict, List, Optional

class TestSuite:
    """Manage test versions and learn from results."""

    def __init__(self, test_versions: List[str], rng: Optional[random.Random] = None) -> None:
        self.test_versions = list(test_versions)
        self.test_results: Dict[str, str] = {}
        self.rng = rng or random.Random()

    def run_test(self, version: str) -> str:
        """Simulate running a test version and record its result."""
        success_rate = self.rng.uniform(0, 1)
        result = "Pass" if success_rate > 0.8 else "Fail"
        self.test_results[version] = result
        return result

    def evaluate_tests(self) -> str:
        """Return the version with the best result."""
        return max(self.test_results, key=self.test_results.get)

    def adjust_tests(self, best_version: str) -> None:
        """Create an improved version based on the best performer."""
        improved_version = f"{best_version}_Improved"
        self.test_versions.append(improved_version)

    def loop_tests(self, iterations: int = 5) -> None:
        """Run tests iteratively, adjusting after each round."""
        for _ in range(iterations):
            for version in list(self.test_versions):
                self.run_test(version)
            best = self.evaluate_tests()
            self.adjust_tests(best)
