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

    def test_validation(self):
        agent = Agent("B")
        with self.assertRaises(ValueError):
            agent.update_emotion(-0.1)
        with self.assertRaises(ValueError):
            agent.update_tension(-0.1)

    def test_capping_and_history(self):
        agent = Agent("C")
        agent.update_emotion(1.2)
        self.assertEqual(agent.emotion, 1.0)
        agent.update_tension(1.5)
        self.assertEqual(agent.tension, 1.0)
        # Lower tension and emotion below threshold so that no transition happens
        agent.update_tension(0.2)
        agent.update_emotion(0.1)
        history_len = len(agent.history)
        agent.transition()
        # No transition should occur because thresholds aren't exceeded
        self.assertEqual(len(agent.history), history_len)


if __name__ == '__main__':
    unittest.main()
