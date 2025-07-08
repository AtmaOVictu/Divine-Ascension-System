import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.interaction import EmotionalNetwork
from divine_agents.karma import Karma


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

    def test_emotional_network(self):
        a1 = Agent("A1", emotion=0.6)
        a2 = Agent("A2", emotion=0.0)
        network = EmotionalNetwork([a1, a2])
        network.set_influence_matrix([[1.0, 0.5], [0.5, 1.0]])
        network.propagate(influence_factor=0.5)
        self.assertGreater(a2.emotion, 0.0)

    def test_karma_update(self):
        class Emotion:
            def __init__(self, **kw):
                for k, v in kw.items():
                    setattr(self, k, v)

        karma = Karma()
        emotion = Emotion(joy=0.9)
        value = karma.update(emotion, 0.0)
        self.assertGreater(value, 0)


if __name__ == '__main__':
    unittest.main()
