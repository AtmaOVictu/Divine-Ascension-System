import unittest
from divine_agents import Agent, OmnipotentAgent, AgentImprovement, SystemAnalysis


class TestOmnipotentAgent(unittest.TestCase):
    def test_assign_supervision(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        omni = OmnipotentAgent("Omni")
        omni.assign_supervision([a1, a2])
        self.assertIn("A1", omni.provide_feedback())

    def test_control_transition(self):
        agent = Agent("A", tension=0.8)
        omni = OmnipotentAgent("Omni")
        omni.control_transition(agent)
        self.assertEqual(agent.state, "Enotnost")

    def test_recommend_improvement(self):
        agent = Agent("B", emotion=-0.6)
        improv = AgentImprovement("Imp")
        msg = improv.recommend_improvement(agent)
        self.assertIn("reducing hate", msg)


class TestSystemAnalysis(unittest.TestCase):
    def test_system_feedback(self):
        a1 = Agent("A1", tension=0.9)
        a2 = Agent("A2", emotion=-0.6)
        analyzer = SystemAnalysis([a1, a2])
        analyzer.analyze_system()
        feedback = analyzer.get_system_feedback()
        self.assertIn("high tension", feedback)
        self.assertIn("negative emotions", feedback)


if __name__ == "__main__":
    unittest.main()
