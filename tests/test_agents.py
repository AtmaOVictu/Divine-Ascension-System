import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.paradoxical_agent import ParadoxicalAgent


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


class TestParadoxicalAgent(unittest.TestCase):
    def test_ask_paradox(self):
        agent = ParadoxicalAgent("P")
        self.assertIn("Ali sem jaz res", agent.ask_paradox())

    def test_paradox_transition(self):
        agent = ParadoxicalAgent("P")
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")
        self.assertIn("Ali sem to", agent.ask_paradox())

if __name__ == "__main__":
    unittest.main()


