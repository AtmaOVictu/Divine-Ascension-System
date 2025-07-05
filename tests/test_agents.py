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

    def test_companion_interaction(self):
        agent = Agent("A", tension=0.6)
        agent.interact_with_shadow()
        self.assertGreater(agent.tension, 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_angel_interaction(self):
        agent = Agent("B", emotion=0.4)
        agent.interact_with_angel()
        self.assertGreater(agent.emotion, 0.4)


if __name__ == '__main__':
    unittest.main()
