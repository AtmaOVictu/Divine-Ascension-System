import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        agent.update_emotion("joy", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

        agent.update_emotion("fear", 0.9)
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("Fear"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # Ensure emotions are reflected in dialogue
        self.assertTrue(any("Anger" in line or "Joy" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
