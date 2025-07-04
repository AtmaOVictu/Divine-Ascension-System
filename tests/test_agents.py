import unittest
from divine_agents import Agent, BinaryAgent, philosophical_dialogue


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

    def test_binary_agent_transition(self):
        b = BinaryAgent(agent_id=1, phase=0, tension=0.6)
        new_phase = b.transition()
        self.assertEqual(new_phase, 1)
        self.assertEqual(b.get_state(), "Aktivacija (1)")


if __name__ == '__main__':
    unittest.main()

