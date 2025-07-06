import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.alphabet import create_alphabet_agents, alphabet_dialogue


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


class TestAlphabetAgents(unittest.TestCase):
    def test_create_alphabet_agents(self):
        agents = create_alphabet_agents()
        self.assertEqual(len(agents), 26)
        self.assertEqual(agents[0].name, "A")

    def test_alphabet_dialogue(self):
        lines = alphabet_dialogue()
        self.assertTrue(any("absolutna" in line for line in lines))
        self.assertTrue(any("relativna" in line for line in lines))
        self.assertTrue(any("eno" in line for line in lines))

if __name__ == "__main__":
    unittest.main()
