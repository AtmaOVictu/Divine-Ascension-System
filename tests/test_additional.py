import unittest

from divine_agents.agent import Agent
from divine_agents.discourse import TruthDiscourse
from divine_agents.phononto import FonontoTransition
from divine_agents.emotions import EMOTIONS


class TestAdditionalModules(unittest.TestCase):
    def test_emotion_levels(self):
        self.assertIn("happiness", EMOTIONS)
        for value in EMOTIONS.values():
            self.assertIn(value, (-1, 0, 1))

    def test_fononto(self):
        trans = FonontoTransition("O", "T")
        meaning = trans.apply_transition()
        self.assertEqual(meaning, "Transformacija")

    def test_truth_discourse(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        disc = TruthDiscourse(a1, a2)
        lines = disc.discuss()
        self.assertTrue(any("Napetost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
