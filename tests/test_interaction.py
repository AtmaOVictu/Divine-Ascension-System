import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.interaction import run_dialogue


class TestInteraction(unittest.TestCase):
    def test_run_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = run_dialogue(a1, a2, "Kaj je resnica?")
        # After running one step, both agents should have transitioned once
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("A1" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
