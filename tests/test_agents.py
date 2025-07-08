import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.rl_agent import RLAgent


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

    def test_rl_agent_policy_update(self):
        agent = RLAgent("R1")
        old_state = agent.state
        agent.update_tension(0.9)
        new_state = agent.transition()
        agent.update_policy(old_state, "respond", 1.0, new_state)
        self.assertIn("respond", agent.q_table[old_state])

    def test_reflection_adjustment(self):
        agent = RLAgent("R2")
        agent.reflect("This caused fear")
        self.assertGreater(agent.tension, 0)


if __name__ == '__main__':
    unittest.main()
