import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.codex import Codex


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

    def test_codex_transition(self):
        codex = Codex()
        codex.transition(1, state_type="True", level=1, pair_type="0 and 1", dimensional_type="D1")
        self.assertIn("True at level 1", codex.get_state())
        self.assertEqual(codex.get_dimensional_state()["SystemAdjustment"], 0.1)


if __name__ == '__main__':
    unittest.main()
