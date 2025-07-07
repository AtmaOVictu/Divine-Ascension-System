import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        # further transition driven by emotion
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

        agent.state = "Ego"
        agent.update_emotion(0.9, "anger")
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("Z zaskrbljenostjo"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # ensure emotional prefixes appear
        self.assertTrue(any("Z zaskrbljenostjo" in line for line in lines if "A1" in line))


if __name__ == '__main__':
    unittest.main()
