import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses_with_emotion(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("Čustveno"))

    def test_dialogue(self):
        a1 = Agent("A1", numerology=1)
        a2 = Agent("A2", state="Jaz", numerology=2)
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("skrito deluje" in line for line in lines))
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_numerology_action(self):
        agent = Agent("A", numerology=3)
        self.assertEqual(agent.numerology_action(), "Explore")


if __name__ == '__main__':
    unittest.main()
