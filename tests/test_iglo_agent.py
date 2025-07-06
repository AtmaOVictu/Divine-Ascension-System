import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.iglo_agent import IgloAgent


def block1(results):
    return "data"


def block2(results):
    return results.get("block1", "") + " processed"


def block3(results):
    return "parallel"


class TestIgloAgent(unittest.TestCase):
    def test_execute(self):
        agent = IgloAgent()
        agent.execute([block1, block2], [block3])
        self.assertEqual(agent.results["block1"], "data")
        self.assertEqual(agent.results["block2"], "data processed")
        self.assertEqual(agent.results["block3"], "parallel")


if __name__ == "__main__":
    unittest.main()
