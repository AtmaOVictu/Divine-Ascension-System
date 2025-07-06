import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.advanced import (
    AgentGenerator,
    ExperienceBasedLearning,
    MultiLayerDecisionMaker,
)


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

    def test_multilayer_decision(self):
        agent = Agent("B", tension=0.8, emotion=0.6)
        decision = MultiLayerDecisionMaker(agent).multi_layer_decision()
        self.assertEqual(decision, "Jaz")

    def test_agent_generator(self):
        gen = AgentGenerator("warrior")
        new_agent = gen.generate_agent()
        self.assertIsInstance(new_agent, Agent)

    def test_learning(self):
        agent = Agent("C")
        agent.add_experience("helped")
        learner = ExperienceBasedLearning(agent)
        result = learner.learn_from_experience("danger")
        self.assertEqual(result, "Act selflessly")


if __name__ == '__main__':
    unittest.main()
