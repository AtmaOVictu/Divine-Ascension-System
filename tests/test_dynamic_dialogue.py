import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent
from divine_agents.dialogue import dynamic_dialogue


class TestDynamicDialogue(unittest.TestCase):
    def test_multi_round_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = dynamic_dialogue(a1, a2, rounds=2)
        # After two rounds both agents should progress at least one state
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)
        self.assertTrue(len(lines) > 0)

    def test_emotional_notes(self):
        a1 = Agent("A1", emotion=0.8)
        response = a1.respond("Kaj je resnica?")
        self.assertIn("Čutim", response)


if __name__ == "__main__":
    unittest.main()
