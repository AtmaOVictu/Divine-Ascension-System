import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.recorder import ShortEgoRecorder


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
        recorder = ShortEgoRecorder()
        lines = philosophical_dialogue(a1, a2, recorder)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(len(recorder.get_records()) >= 2)

    def test_recorder_limitations(self):
        agent = Agent("B")
        recorder = ShortEgoRecorder()
        # Agent remains in Ego due to low emotion, this should register a limitation
        state = agent.transition()
        recorder.record_transition(agent, state)
        self.assertTrue(recorder.get_limitations())


if __name__ == '__main__':
    unittest.main()
