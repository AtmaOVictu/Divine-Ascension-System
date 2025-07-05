import unittest

from divine_agents.agent import Agent
from divine_agents.omnipotent import OmnipotentAgent


class TestOmnipotentAgent(unittest.TestCase):
    def test_supervision_and_feedback(self):
        agent_a = Agent("A")
        agent_b = Agent("B")
        omni = OmnipotentAgent("Omni")
        omni.assign_supervision([agent_a, agent_b])
        agent_a.history.append("compete")
        agent_b.history.append("cooperate")
        agent_a.update_emotion(-1.0)
        agent_b.update_emotion(1.0)
        omni.analyze_agents()
        feedback = omni.provide_feedback()
        self.assertIn("competitive", feedback)
        self.assertIn("positive emotions", feedback)

    def test_control_transition(self):
        agent = Agent("A", tension=0.8)
        omni = OmnipotentAgent("Omni")
        omni.control_transition(agent)
        self.assertEqual(agent.state, "Enotnost")
        self.assertIn("directed", agent.history[-1])


if __name__ == "__main__":
    unittest.main()
