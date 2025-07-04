import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_from_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_from_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.9)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("C", state="Enotnost", emotion=0.2)
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("Mirno"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)


if __name__ == '__main__':
    unittest.main()
