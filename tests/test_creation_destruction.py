import unittest
from divine_agents.creation_destruction import CreativeAgent, DestructiveAgent, interaction

class TestCreationDestruction(unittest.TestCase):
    def test_interaction_transitions(self):
        creator = CreativeAgent("Creator")
        destroyer = DestructiveAgent("Destroyer")
        lines = interaction(creator, destroyer)
        self.assertIn("Creator prehaja v stanje", lines[2])
        self.assertIn("Destroyer prehaja v stanje", lines[3])
        self.assertIn(creator.state, creator.STATES)
        self.assertIn(destroyer.state, destroyer.STATES)

    def test_state_change_by_emotion(self):
        agent = DestructiveAgent("D")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

if __name__ == '__main__':
    unittest.main()
