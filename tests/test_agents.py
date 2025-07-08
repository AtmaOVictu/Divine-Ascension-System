import unittest


from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.emotions import Emotion, Karma, AgentGroup


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

    def test_emotional_transition(self):
        e = Emotion(despair=0.9)
        e.transition()
        self.assertGreater(e.hope, 0)
        self.assertLess(e.despair, 0.9)

    def test_karma_tracking(self):
        e = Emotion(joy=0.9)
        k = Karma()
        val = k.update(e, [[0.0, 0.0], [0.0, 0.0]])
        self.assertGreater(val, 0)
        self.assertEqual(len(k.track_karma_over_time()), 1)

    def test_emotional_contagion(self):
        group = AgentGroup(2)
        group.emotions = [1.0, -1.0]
        influence = [[0.0, 1.0], [1.0, 0.0]]
        group.update_emotions(influence, influence_factor=0.5)
        self.assertTrue(all(abs(val) <= 1 for val in group.emotions))


if __name__ == '__main__':
    unittest.main()
