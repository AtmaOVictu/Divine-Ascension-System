import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, simulate_conversation


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

    def test_simulate_conversation(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        transcript = simulate_conversation(a1, a2, rounds=3)
        # After multiple rounds, at least one agent should reach Enotnost
        self.assertIn("Enotnost", a1.state + a2.state)
        self.assertTrue(any("prehaja" in line for line in transcript))


if __name__ == '__main__':
    unittest.main()
