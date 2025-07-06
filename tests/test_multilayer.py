import unittest
from divine_agents import Agent, MultiLayerTransitionSystem, ExperienceBasedLearning


class TestMultiLayerTransition(unittest.TestCase):
    def test_multi_layer_transition(self):
        agent = Agent("A")
        ml = MultiLayerTransitionSystem(agent)
        agent.update_tension(0.8)
        state = ml.multi_layer_transition()
        self.assertEqual(state, "Jaz")

    def test_loyalty_transition(self):
        agent = Agent("B", state="Jaz", loyalty=0.9)
        agent.record_experience("cooperative")
        ml = MultiLayerTransitionSystem(agent)
        state = ml.multi_layer_transition()
        self.assertEqual(state, "Enotnost")


class TestExperienceBasedLearning(unittest.TestCase):
    def test_learning_decision(self):
        agent = Agent("L")
        learner = ExperienceBasedLearning(agent)
        learner.update_experience("dialogue", 1)
        decision = learner.decide("dialogue")
        self.assertEqual(decision, "Act selflessly")


if __name__ == "__main__":
    unittest.main()
