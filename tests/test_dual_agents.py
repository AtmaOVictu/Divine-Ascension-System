import unittest
from divine_agents.dual_agents import CreativeAgent, DestructiveAgent, creative_destructive_interaction


class TestDualAgents(unittest.TestCase):
    def test_create_and_destroy_karma(self):
        creator = CreativeAgent("C")
        destroyer = DestructiveAgent("D")
        creator.create()
        destroyer.destroy()
        self.assertGreater(creator.karma, 0)
        self.assertLess(destroyer.karma, 0)

    def test_interaction_triggers_transitions(self):
        creator = CreativeAgent("C")
        destroyer = DestructiveAgent("D")
        lines = creative_destructive_interaction(creator, destroyer)
        # After actions, at least one agent should have transitioned
        transitioned = any(state in line for state in ("Jaz", "Enotnost") for line in lines)
        self.assertTrue(transitioned)


if __name__ == "__main__":
    unittest.main()
