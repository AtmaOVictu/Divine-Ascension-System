import unittest
from divine_agents.agent import Agent, logistic_function
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_evolve_increases_tension(self):
        agent = Agent("A")
        agent.update_emotion(0.8)
        before = agent.tension
        agent.evolve()
        self.assertGreater(agent.tension, before)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_logistic_function(self):
        self.assertAlmostEqual(logistic_function(0.5), 0.5, delta=0.1)


if __name__ == '__main__':
    unittest.main()
