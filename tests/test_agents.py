import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.environment import Environment


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
        env = Environment(pressure=0.8)
        lines = philosophical_dialogue(a1, a2, env)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_environment_influence(self):
        env = Environment(pressure=0.9)
        agent = Agent("B")
        env.influence(agent)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")


if __name__ == '__main__':
    unittest.main()
