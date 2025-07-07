import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
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

    def test_emotion_only_triggers_transition_ego_to_jaz(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_only_triggers_transition_jaz_to_enotnost(self):
        agent = Agent("C", state="Jaz")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_no_transition_below_thresholds(self):
        agent = Agent("D")
        agent.update_emotion(0.5)
        state = agent.transition()
        self.assertEqual(state, "Ego")
        agent.update_tension(0.7)
        state = agent.transition()
        self.assertEqual(state, "Ego")


if __name__ == '__main__':
    unittest.main()
