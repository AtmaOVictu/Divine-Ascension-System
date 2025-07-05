import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        agent.update_emotion(0.9, "veselje")
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Ego")
        agent.update_emotion(0.6, "strah")
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("S strahom"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("S strahom" in line for line in lines))
        self.assertTrue(any("Z veseljem" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
