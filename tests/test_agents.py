import unittest
import sys
from pathlib import Path

# Ensure project root is on the import path so tests can be run from any CWD
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_second_transition_by_emotion(self):
        agent = Agent("B", state="Jaz")
        agent.update_emotion(0.6)
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

    def test_response_text(self):
        ego = Agent("E", state="Ego")
        self.assertEqual(ego.respond("?"), "Resnica je absolutna in neodvisna od drugih.")
        jaz = Agent("J", state="Jaz")
        self.assertEqual(jaz.respond("?"), "Resnica je relativna, oblikovana z našimi odnosi.")
        eno = Agent("En", state="Enotnost")
        self.assertEqual(eno.respond("?"), "Vse resnice so eno, medsebojno povezane.")


if __name__ == '__main__':
    unittest.main()
