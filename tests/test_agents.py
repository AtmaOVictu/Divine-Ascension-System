import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.tracker import Tracker


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
        tracker = Tracker()
        lines = philosophical_dialogue(a1, a2, tracker)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_tracker_records(self):
        tracker = Tracker()
        agent = Agent("T", tracker=tracker)
        agent.update_tension(0.9)
        agent.transition()
        self.assertEqual(tracker.history("T"), ["Ego", "Jaz"])

    def test_transition_by_emotion(self):
        agent = Agent("E")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")


if __name__ == '__main__':
    unittest.main()
