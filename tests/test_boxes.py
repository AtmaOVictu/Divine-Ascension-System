import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue_boxed
from divine_agents.boxes import SymbolicBox


class TestSymbolicBoxes(unittest.TestCase):
    def test_boxed_dialogue_flow(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        boxes = philosophical_dialogue_boxed(a1, a2)
        stages = [box.stage for box in boxes]
        self.assertEqual(stages, ["∴", "∆", "⊘"])
        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("Vse resnice" in line for line in boxes[-1].data["dialogue"]))


if __name__ == '__main__':
    unittest.main()
