import unittest
from unittest.mock import Mock
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.time_utils import get_local_time, get_time_from_ip


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


class TestTimeUtilities(unittest.TestCase):
    def test_get_local_time(self):
        time_str = get_local_time()
        self.assertEqual(len(time_str.split()), 2)

    def test_get_time_from_ip(self):
        mock_get = Mock()
        mock_get.side_effect = [
            {"timezone": "Europe/Ljubljana", "city": "Ljubljana"},
            {"datetime": "2023-01-01T12:34:56+01:00"},
        ]
        city, tz, current = get_time_from_ip(mock_get)
        self.assertEqual(city, "Ljubljana")
        self.assertEqual(tz, "Europe/Ljubljana")
        self.assertEqual(current, "2023-01-01T12:34:56+01:00")


if __name__ == '__main__':
    unittest.main()
