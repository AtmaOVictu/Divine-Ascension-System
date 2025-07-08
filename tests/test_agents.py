import unittest
from divine_agents import Agent, RLAgent, philosophical_dialogue


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


class TestRLAgent(unittest.TestCase):
    def test_policy_update_and_reflection(self):
        rl = RLAgent("RL")
        rl.update_policy("Ego", "question", reward=5, next_state="Ego")
        self.assertGreaterEqual(rl.emotion, 0.1)
        rl.reflect("fear")
        self.assertGreater(rl.tension, 0.0)

    def test_rl_transition(self):
        rl = RLAgent("RL")
        rl.update_emotion(0.6)
        rl.transition()
        self.assertEqual(rl.state, "Jaz")


if __name__ == '__main__':
    unittest.main()
