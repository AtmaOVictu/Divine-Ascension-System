import unittest

from divine_agents.agent import Agent
from divine_agents.concurrent import run_parallel_dialogues


class TestParallelDialogues(unittest.TestCase):
    def test_parallel_runs(self):
        pairs = [
            (Agent("A1"), Agent("A2", state="Jaz")),
            (Agent("B1", state="Jaz"), Agent("B2")),
        ]
        results = run_parallel_dialogues(pairs)
        self.assertEqual(len(results), 2)
        for transcript in results:
            self.assertTrue(any("prehaja v stanje" in line for line in transcript))


if __name__ == "__main__":
    unittest.main()
