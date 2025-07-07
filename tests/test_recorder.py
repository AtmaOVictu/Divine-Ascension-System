import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent
from divine_agents.recorder import ShortEgoRecorder
from divine_agents.dialogue import philosophical_dialogue


class TestRecorder(unittest.TestCase):
    def test_record_transition_and_limitation(self):
        agent = Agent("A")
        recorder = ShortEgoRecorder()
        agent.update_emotion(0.2)
        new_state = agent.transition()
        recorder.record_transition(agent, new_state)
        self.assertEqual(len(recorder.get_records()), 1)
        self.assertTrue(any("low emotion" in l for l in recorder.get_limitations()))

    def test_dialogue_records(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        recorder = ShortEgoRecorder()
        philosophical_dialogue(a1, a2, recorder)
        # Should capture at least two transitions
        self.assertGreaterEqual(len(recorder.get_records()), 2)


if __name__ == "__main__":
    unittest.main()
