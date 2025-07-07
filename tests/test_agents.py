import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, multi_turn_dialogue


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

    def test_emotion_drives_transitions_over_turns(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = multi_turn_dialogue(a1, a2, turns=3, emotion_step=0.3)

        # After three emotion updates tension should be 0.9 and state should change
        self.assertAlmostEqual(a1.tension, 0.9, places=2)
        self.assertEqual(a1.state, "Jaz")

        # Dialogue lines should reflect agent states after each turn
        for turn in range(3):
            self.assertIn(f"({a1.history[turn]})", lines[turn * 4])
            self.assertIn(f"({a2.history[turn]})", lines[turn * 4 + 1])


if __name__ == '__main__':
    unittest.main()
