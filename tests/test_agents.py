import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from divine_agents import Agent, philosophical_dialogue, ontological_debate


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

    def test_ontological_debate_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        history = ontological_debate(a1, a2, rounds=3)
        # After several rounds tension should cause transitions
        self.assertIn("Jaz", a1.history)
        self.assertIn("Enotnost", a2.history)

    def test_speak_includes_emotion(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        text = agent.speak()
        self.assertIn("mo\u010dna", text)


if __name__ == '__main__':
    unittest.main()
