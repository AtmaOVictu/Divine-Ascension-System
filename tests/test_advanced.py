import random
import unittest

from divine_agents.agent import Agent
from divine_agents.advanced import (
    MultiLayerDecisionMaker,
    ExperienceBasedLearning,
    AgentGenerator,
)


class TestAdvancedFeatures(unittest.TestCase):
    def test_multi_layer_decision(self):
        agent = Agent("A")
        agent.loyalty = 0.9
        agent.update_tension(0.8)
        decision_maker = MultiLayerDecisionMaker(agent)
        state = decision_maker.multi_layer_decision()
        self.assertEqual(state, "Jaz")

    def test_learning(self):
        agent = Agent("A")
        agent.history.append("helped")
        learner = ExperienceBasedLearning(agent)
        action = learner.learn_from_experience("danger")
        self.assertEqual(action, "Act selflessly")

    def test_agent_generation(self):
        random.seed(0)
        generator = AgentGenerator("warrior")
        new_agent = generator.generate_agent()
        self.assertIn(new_agent.state, Agent.STATES)
        self.assertTrue(0 <= new_agent.loyalty <= 1)


if __name__ == "__main__":
    unittest.main()
