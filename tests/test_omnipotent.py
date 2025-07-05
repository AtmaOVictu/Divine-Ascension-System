import unittest
from divine_agents import Agent, OmnipotentAgent, LoadingScreenUnity


class TestOmnipotentAgent(unittest.TestCase):
    def test_control_transition(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        omni = OmnipotentAgent("Omni")
        omni.control_transition(agent)
        self.assertEqual(agent.state, "Enotnost")
        self.assertIn("Omni directed", agent.history[-1])

    def test_analysis_feedback(self):
        a1 = Agent("A1", emotion=-1)
        omni = OmnipotentAgent("Omni")
        omni.assign_supervision([a1])
        omni.analyze_agents()
        feedback = omni.provide_feedback()
        self.assertIn("negative emotions", feedback)


class TestLoadingScreenUnity(unittest.TestCase):
    def test_cycle(self):
        loader = LoadingScreenUnity("Agent")
        for _ in range(99):
            loader.update()
        self.assertAlmostEqual(loader.unity_value, 0.01, places=2)


if __name__ == "__main__":
    unittest.main()
