import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        agent.evolve()
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_set_parameters(self):
        agent = Agent("A")
        agent.set_parameters(k_bio=2.0)
        self.assertEqual(agent.k_bio, 2.0)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_get_state(self):
        agent = Agent("A")
        state = agent.get_state()
        self.assertEqual(len(state), 2)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertIn(a1.state, Agent.STATES)


if __name__ == '__main__':
    unittest.main()
