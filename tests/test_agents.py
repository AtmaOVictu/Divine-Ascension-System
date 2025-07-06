import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
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

    def test_dialogue_sequence(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")

        # verify initial states
        self.assertEqual(a1.state, "Ego")
        self.assertEqual(a2.state, "Jaz")

        lines = philosophical_dialogue(a1, a2)

        # expected dialogue lines
        expected = [
            "A1 (Ego): Resnica je absolutna in neodvisna od drugih.",
            "A2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.",
            "A1 prehaja v stanje: Jaz",
            "A2 prehaja v stanje: Enotnost",
            "A1: Resnica je relativna, oblikovana z našimi odnosi.",
            "A2: Vse resnice so eno, medsebojno povezane.",
        ]
        self.assertEqual(lines, expected)

        # verify transitions recorded in history
        self.assertEqual(a1.history, ["Ego", "Jaz"])
        self.assertEqual(a2.history, ["Jaz", "Enotnost"])

        # verify final states
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")

        # verify responses according to final states
        self.assertEqual(a1.respond("Kaj je resnica?"),
                         "Resnica je relativna, oblikovana z našimi odnosi.")
        self.assertEqual(a2.respond("Kaj je resnica?"),
                         "Vse resnice so eno, medsebojno povezane.")


if __name__ == '__main__':
    unittest.main()
