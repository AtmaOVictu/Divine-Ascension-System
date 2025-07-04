import unittest
from divine_agents.agent import Agent
from divine_agents.opposite_agent import OppositeAgent
from divine_agents.dialogue import philosophical_dialogue, opposing_dialogue


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


class TestOppositeAgent(unittest.TestCase):
    def test_contradiction_transition(self):
        agent = OppositeAgent("B")
        state = agent.contradiction_transition(0.8)
        self.assertEqual(state, "Jaz")

    def test_opposing_dialogue(self):
        a1 = OppositeAgent("O1")
        a2 = OppositeAgent("O2", state="Jaz")
        lines = opposing_dialogue(a1, a2)
        self.assertTrue(any("Jaz" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
