import unittest
from divine_agents import Agent, Codex


class TestCodex(unittest.TestCase):
    def test_codex_debate_triggers_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        codex = Codex()
        codex.register(a1)
        codex.register(a2)
        lines = codex.debate(a1, a2)
        # After debate, at least one agent should reach 'Enotnost'
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_no_transition_below_threshold(self):
        agent = Agent("B", tension=0.5, emotion=0.4)
        agent.transition()
        self.assertEqual(agent.state, "Ego")


if __name__ == "__main__":
    unittest.main()
