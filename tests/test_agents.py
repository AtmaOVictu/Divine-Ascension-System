import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.alphabet_system import create_alphabet_agents, transition_all


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

    def test_alphabet_system(self):
        agents = create_alphabet_agents()
        self.assertEqual(len(agents), 26)
        transition_all(agents)
        states = {agent.state for agent in agents}
        # At least one agent should have progressed beyond Ego
        self.assertTrue(any(state != "Ego" for state in states))


if __name__ == '__main__':
    unittest.main()
