import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_below_thresholds(self):
        agent = Agent("B")
        agent.update_tension(0.6)
        agent.emotion = 0.4  # does not raise tension above threshold
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.set_emotion("joy", 0.2)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("joy", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # ensure emotion tags are in dialogue
        self.assertTrue(any("občutek" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
