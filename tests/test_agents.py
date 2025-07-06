import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.alphabet import create_alphabet_agents, run_alphabet_dialogues


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

    def test_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertIn("Jaz", a1.state)
        self.assertIn("Enotnost", a2.state)
        self.assertTrue(any("Resnica" in line for line in lines))


class TestAlphabetAgents(unittest.TestCase):
    def test_create_alphabet_agents(self):
        agents = create_alphabet_agents()
        self.assertEqual(len(agents), 26)
        self.assertTrue(all(agent.state == "Ego" for agent in agents))

    def test_alphabet_dialogues(self):
        lines = run_alphabet_dialogues()
        self.assertTrue(any("prehaja" in line for line in lines))
        self.assertTrue(any("Resnica" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
