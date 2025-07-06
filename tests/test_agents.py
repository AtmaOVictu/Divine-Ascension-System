import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.relative_absolutes import RelativeAbsoluteLibrary


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

    def test_absolute_library(self):
        lib = RelativeAbsoluteLibrary()
        val = lib.get_absolute("truth")
        self.assertTrue(0.5 <= val <= 1.5)

    def test_evolve(self):
        agent = Agent("A")
        agent.update_emotion(0.9)
        state = agent.evolve()
        self.assertEqual(state, "Jaz")


if __name__ == '__main__':
    unittest.main()
