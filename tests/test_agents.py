import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion("fear", 0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_tension_triggers_transition(self):
        agent = Agent("B")
        agent.update_tension(0.9)
        self.assertEqual(agent.transition(), "Jaz")

    def test_no_transition_below_thresholds(self):
        agent = Agent("C")
        agent.update_emotion("joy", 0.4)
        self.assertEqual(agent.transition(), "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("čustvo", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # Ensure emotion information is included in dialogue
        self.assertTrue(any("čustvo" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
