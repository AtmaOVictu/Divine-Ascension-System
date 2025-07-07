import unittest
from unittest import mock

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.krak import Krak, KrakManager


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_jaz_to_enotnost(self):
        agent = Agent("A", state="Jaz")
        agent.update_tension(0.9)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertIn(a1.state, ["Jaz", "Enotnost"])
        self.assertIn(a2.state, ["Enotnost"])


class TestKrakManager(unittest.TestCase):
    @mock.patch("divine_agents.krak.request.urlopen")
    @mock.patch("random.random", return_value=0.9)
    def test_distribute_krak(self, mock_random, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = b"ok"
        manager = KrakManager()
        manager.add_krak(Krak("T1", "test"))
        msg = manager.distribute_krak()
        self.assertIn("activated", msg)

    @mock.patch("random.random", return_value=0.1)
    def test_no_krak_distributed(self, mock_random):
        manager = KrakManager()
        manager.add_krak(Krak("T2", "test"))
        msg = manager.distribute_krak()
        self.assertEqual(msg, "No kraks to distribute.")


if __name__ == "__main__":
    unittest.main()
