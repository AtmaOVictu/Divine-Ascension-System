import unittest
from divine_agents.agent import Agent
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

    def test_dialogue_includes_state_prefix_after_transition(self):
        """Ensure dialogue lines after transitions show the agent's state."""
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = philosophical_dialogue(a1, a2)
        # The last two lines should include the updated state in parentheses
        last_lines = lines[-2:]
        for agent, line in zip((a1, a2), last_lines):
            self.assertTrue(
                line.startswith(f"{agent.name} ({agent.state})"),
                msg=f"Line '{line}' missing state prefix",
            )


if __name__ == '__main__':
    unittest.main()
