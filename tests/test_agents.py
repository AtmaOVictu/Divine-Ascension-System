import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion("fear", 0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_responses(self):
        for state in Agent.STATES:
            agent = Agent("A", state=state)
            reply = agent.respond("Kaj je resnica?")
            self.assertIsInstance(reply, str)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
