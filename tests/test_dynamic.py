import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import dynamic_philosophical_debate


class TestDynamicDialogue(unittest.TestCase):
    def test_debate_triggers_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dynamic_philosophical_debate(a1, a2, rounds=2)
        # After sufficient emotion updates agents should transition
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)
        self.assertTrue(any("prehaja v stanje" in l for l in lines))

    def test_emotional_output(self):
        a1 = Agent("A1", emotion_type="fear")
        a2 = Agent("A2", state="Jaz", emotion_type="joy")
        lines = dynamic_philosophical_debate(a1, a2, rounds=1)
        joined = "\n".join(lines)
        self.assertIn("fear", joined)
        self.assertIn("joy", joined)


if __name__ == '__main__':
    unittest.main()
