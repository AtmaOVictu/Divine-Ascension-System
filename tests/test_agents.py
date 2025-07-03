import unittest
from divine_agents import Agent, ResonanceAgent
from divine_agents.dialogue import philosophical_dialogue


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
        self.assertTrue(any("absolutna" in line for line in lines))
        self.assertTrue(any("relativna" in line for line in lines))

    def test_resonance_transition(self):
        agent = ResonanceAgent("R")
        agent.update_tension(0.8)
        state = agent.resonance_transition()
        self.assertEqual(state, "Jaz")
        self.assertEqual(agent.emotion_name, "anger")

    def test_memory(self):
        agent = ResonanceAgent("M")
        agent.update_tension(0.8)
        agent.resonance_transition()
        self.assertEqual(agent.recall_memory(), ["Ego", "Jaz"])


if __name__ == '__main__':
    unittest.main()
