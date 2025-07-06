import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import PhilosophicalDialogue


class TestAgentSystem(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_emotional_adjustment(self):
        agent = Agent("A")
        agent.set_emotional_state("anger", 0.9)
        self.assertGreater(agent.tension, 0.0)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        dialog = PhilosophicalDialogue(a1, a2)
        lines = dialog.exchange("Kaj je resnica?")
        self.assertTrue(any("absolutna" in line for line in lines))
        self.assertTrue(any("relativna" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
