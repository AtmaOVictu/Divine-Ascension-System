import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.creative_destructive import CreativeAgent, DestructiveAgent, interact


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


class TestCreativeDestructive(unittest.TestCase):
    def test_interaction_transitions_and_karma(self):
        creator = CreativeAgent("Creator")
        destroyer = DestructiveAgent("Destroyer")
        lines = interact(creator, destroyer)
        self.assertEqual(creator.karma, 10)
        self.assertEqual(destroyer.karma, -10)
        self.assertIn(creator.state, ("Jaz", "Enotnost"))
        self.assertIn(destroyer.state, ("Jaz", "Enotnost"))
        combined = " ".join(lines)
        self.assertTrue("absolutna" in combined or "relativna" in combined)


if __name__ == '__main__':
    unittest.main()
