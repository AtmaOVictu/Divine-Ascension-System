import unittest
from divine_agents.iglo_agent import IgloAgent


def block_a(results):
    return "A"


def block_b(results):
    assert "block_a" in results
    return results["block_a"] + "B"


def block_c(results):
    return "C"


class TestIgloAgent(unittest.TestCase):
    def test_sequence_and_parallel(self):
        agent = IgloAgent()
        seq = [block_a, block_b]
        par = [block_c]
        results = agent.execute(seq, par)
        self.assertEqual(results["block_a"], "A")
        self.assertEqual(results["block_b"], "AB")
        self.assertEqual(results["block_c"], "C")


if __name__ == "__main__":
    unittest.main()
