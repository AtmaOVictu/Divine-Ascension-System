import unittest
from divine_agents import (
    Agent,
    MultiLayerDecisionMaker,
    ExperienceBasedLearning,
    AgentGenerator,
)


class TestAdvancedModules(unittest.TestCase):
    def test_multi_layer_decision(self):
        agent = Agent("A", tension=0.8, emotion=0.9, loyalty=0.9)
        decider = MultiLayerDecisionMaker(agent)
        state = decider.decide()
        self.assertEqual(state, "Jaz")

    def test_experience_learning(self):
        agent = Agent("B", experiences=["helped"])
        learner = ExperienceBasedLearning(agent)
        decision = learner.learn("danger")
        self.assertEqual(decision, "Act selflessly")
        self.assertGreater(agent.loyalty, 0.5)

    def test_agent_generator(self):
        gen = AgentGenerator("warrior")
        agent = gen.generate_agent()
        self.assertIsInstance(agent, Agent)
        self.assertGreaterEqual(agent.loyalty, 0)
        self.assertLessEqual(agent.loyalty, 1)


if __name__ == "__main__":
    unittest.main()
