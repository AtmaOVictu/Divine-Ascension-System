import unittest
from divine_agents import (
    Agent,
    MultiLayerDecisionMaker,
    ExperienceBasedLearning,
    AgentGenerator,
)


class TestDecisionMaker(unittest.TestCase):
    def test_multi_layer_decision(self):
        agent = Agent("A")
        agent.emotion = 0.8
        agent.tension = 0.8
        dm = MultiLayerDecisionMaker(agent)
        self.assertEqual(dm.multi_layer_decision(), "Prehod v Ego")


class TestLearning(unittest.TestCase):
    def test_learn_from_experience(self):
        agent = Agent("B")
        agent.history.append("helped")
        learner = ExperienceBasedLearning(agent)
        self.assertEqual(learner.learn_from_experience("danger"), "Act selflessly")


class TestGenerator(unittest.TestCase):
    def test_generate_agent(self):
        gen = AgentGenerator()
        new_agent = gen.generate_agent()
        self.assertIsInstance(new_agent, Agent)
        self.assertTrue(hasattr(new_agent, "loyalty"))


if __name__ == "__main__":
    unittest.main()
