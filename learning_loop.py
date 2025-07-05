import random
from typing import List


class LearningSuite:
    """Iterate over multiple test versions and learn from results."""

    def __init__(self, test_versions: List[str]):
        self.test_versions = list(test_versions)
        self.test_results = {}

    def run_test(self, version: str) -> str:
        """Simulate running a test version and return Pass/Fail."""
        success_rate = random.uniform(0, 1)
        result = "Pass" if success_rate > 0.8 else "Fail"
        self.test_results[version] = result
        return result

    def evaluate_tests(self) -> str:
        """Return the best performing test version."""
        best_version = max(self.test_results, key=self.test_results.get)
        return best_version

    def adjust_tests(self, best_version: str) -> None:
        """Learn from the best version and create a new improved one."""
        improved = f"{best_version}_Improved"
        self.test_versions.append(improved)

    def loop_tests(self, iterations: int = 5) -> None:
        """Run the test loop for a number of iterations."""
        for _ in range(iterations):
            for version in list(self.test_versions):
                self.run_test(version)
            best = self.evaluate_tests()
            self.adjust_tests(best)
            self.test_results.clear()


if __name__ == "__main__":
    versions = ["Test_Version_1", "Test_Version_2", "Test_Version_3"]
    suite = LearningSuite(versions)
    suite.loop_tests()
    print("Final test versions:", suite.test_versions)
