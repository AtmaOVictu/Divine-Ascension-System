import unittest

from divine_agents.agent import Agent, EMOTION_THRESHOLD, TENSION_THRESHOLD
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(TENSION_THRESHOLD + 0.1)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_emotion_prefix(self):
        agent = Agent("X", state="Ego")
        agent.update_emotion(EMOTION_THRESHOLD + 0.1)
        line = agent.respond("?")
        self.assertTrue(line.endswith("!"))


if __name__ == '__main__':
    unittest.main()
