import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, tracked_philosophical_dialogue
from divine_agents.tracker import OntologicalTracker


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

    def test_emotion_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_tracker_records(self):
        a = Agent("T")
        tracker = OntologicalTracker([a])
        tracker.update_agent("T", emotion=0.8)
        self.assertEqual(tracker.transitions[0]["to"], "Jaz")

    def test_tracked_dialogue(self):
        a1 = Agent("D1")
        a2 = Agent("D2", state="Jaz")
        tracker = OntologicalTracker([a1, a2])
        lines = tracked_philosophical_dialogue(a1, a2, tracker)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertGreaterEqual(len(tracker.transitions), 2)


if __name__ == '__main__':
    unittest.main()
