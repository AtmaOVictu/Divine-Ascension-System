import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent, VersionedAgent
from divine_agents.dialogue import philosophical_dialogue


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

    def test_version_transition(self):
        a1 = VersionedAgent("A1", emotion=0.4)
        a2 = Agent("A2", state="Jaz")
        a1.touch(a2)
        self.assertEqual(a1.version, "verzija 2")
        self.assertEqual(a1.state, "Jaz")

    def test_versioned_dialogue(self):
        a1 = VersionedAgent("A1")
        a2 = VersionedAgent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("verzija" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
