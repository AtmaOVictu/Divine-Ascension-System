import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import (
    philosophical_dialogue,
    deep_thought_dialogue,
)
from divine_agents.ontology import DEEP_THOUGHT_KEY, DEEP_THOUGHT_LANGUAGE


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


class TestDeepThought(unittest.TestCase):
    def test_key_setup(self):
        self.assertEqual(DEEP_THOUGHT_KEY.ontological_key, "deep_thought_mode")
        self.assertIn("philosophical_analysis", DEEP_THOUGHT_KEY.tools_enabled)

    def test_deep_thought_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = deep_thought_dialogue(a1, a2)
        self.assertTrue(
            any(DEEP_THOUGHT_LANGUAGE.symbolism["resolve"] in line for line in lines)
        )


if __name__ == "__main__":
    unittest.main()
