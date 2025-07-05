import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, philosophical_debate


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

    def test_emotion_setting(self):
        agent = Agent("B")
        agent.set_emotion("fear", 0.6)
        self.assertEqual(agent.emotion_label, "fear")
        self.assertGreater(agent.tension, 0.5)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_debate_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2, rounds=1)
        # After debate round emotions should trigger a transition for agent1
        self.assertIn(a1.state, ("Jaz", "Enotnost"))
        self.assertTrue(any("prehaja" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
