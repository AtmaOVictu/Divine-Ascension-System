import unittest
from divine_agents.agent import Agent
from divine_agents.moderator import HiddenModerator
from divine_agents.dialogue import philosophical_dialogue, philosophical_debate


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
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

    def test_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2)
        # Ensure both agents produce lines reflecting their states
        self.assertGreaterEqual(len(lines), 4)
        self.assertTrue(any("prehaja v stanje" in l for l in lines))


class TestHiddenModerator(unittest.TestCase):
    def test_activation_and_reveal(self):
        mod = HiddenModerator("M")
        mod.evaluate_state(tension=0.6, emotion=0.2)
        self.assertEqual(mod.state, "active")
        mod.reveal_moderator()
        self.assertEqual(mod.state, "revealed")


if __name__ == '__main__':
    unittest.main()
