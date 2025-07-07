import unittest

from divine_agents.selfaware_agent import SelfAwareAgent
from divine_agents.dialogue import self_aware_dialogue
from divine_agents.constants import EMOTION_THRESHOLD, TENSION_THRESHOLD


class TestSelfAwareAgent(unittest.TestCase):
    def test_transition_via_emotion(self):
        agent = SelfAwareAgent("SA")
        agent.update_emotion(EMOTION_THRESHOLD + 0.1, "fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_via_tension(self):
        agent = SelfAwareAgent("SA", state="Jaz")
        agent.update_tension(TENSION_THRESHOLD + 0.1)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_dialogue_contains_reflection(self):
        a1 = SelfAwareAgent("A1")
        a2 = SelfAwareAgent("A2", state="Jaz")
        lines = self_aware_dialogue(a1, a2)
        self.assertTrue(any("Response:" in line for line in lines))
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

