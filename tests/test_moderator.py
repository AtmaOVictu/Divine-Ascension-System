import unittest
from divine_agents.moderator import HiddenModerator, LatentAgent


class TestHiddenModerator(unittest.TestCase):
    def test_activation_and_reveal(self):
        mod = HiddenModerator("M")
        mod.evaluate_state(tension=0.6, emotion=0.6)
        self.assertEqual(mod.state, "active")
        mod.reveal_moderator()
        self.assertEqual(mod.state, "revealed")


class TestLatentAgent(unittest.TestCase):
    def test_latent_activation(self):
        agent = LatentAgent("L")
        agent.evaluate_state(tension=0.6)
        self.assertEqual(agent.state, "active")
        agent.reveal_agent()
        self.assertEqual(agent.state, "revealed")


if __name__ == "__main__":
    unittest.main()
