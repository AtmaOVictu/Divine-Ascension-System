import random
from typing import List

class LearningTestSuite:
    """Simulate running multiple versions of tests and learning from results."""

    def __init__(self, test_versions: List[str]):
        self.test_versions = test_versions
        self.test_results = {}

    def run_test(self, version: str) -> str:
        """Run a test version and record pass/fail."""
        print(f"Running Test Version: {version}")
        success_rate = random.uniform(0, 1)
        result = "Pass" if success_rate > 0.8 else "Fail"
        self.test_results[version] = result
        return result

    def evaluate_tests(self) -> str:
        """Return the best performing test version."""
        best_version = max(self.test_results, key=self.test_results.get)
        print(
            f"Best performing test version: {best_version} with result {self.test_results[best_version]}"
        )
        return best_version

    def adjust_tests(self, best_version: str) -> None:
        """Learn from the best version and create an improved one."""
        improved = f"{best_version}_Improved"
        self.test_versions.append(improved)
        print(f"Adjusting tests based on {best_version}... New version: {improved}")

    def loop_tests(self, iterations: int = 5) -> None:
        """Loop through test versions for a number of iterations."""
        for i in range(iterations):
            print(f"\nIteration {i + 1}/{iterations}...")
            for version in list(self.test_versions):
                result = self.run_test(version)
                print(f"Test {version}: {result}")
            best_version = self.evaluate_tests()
            self.adjust_tests(best_version)


if __name__ == "__main__":
    versions = ["Test_Version_1", "Test_Version_2", "Test_Version_3"]
    suite = LearningTestSuite(versions)
    suite.loop_tests()
