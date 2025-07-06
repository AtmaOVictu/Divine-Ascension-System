import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.system import (
    EmotionalTensionDynamics,
    MultiLayerTransitionSystem,
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

    def test_emotional_tension_dynamics(self):
        agent = Agent("A")
        agent.update_emotional_state("angry", 0.1)
        EmotionalTensionDynamics(agent).adjust_tension_based_on_emotions()
        self.assertGreater(agent.tension, 0.1)

    def test_multilayer_transition(self):
        agent = Agent("A", emotional_state="fearful", tension=0.8)
        system = MultiLayerTransitionSystem(agent)
        state = system.multi_layer_transition()
        self.assertEqual(state, "Ego")


if __name__ == '__main__':
    unittest.main()
