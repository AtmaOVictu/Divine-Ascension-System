import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.symbolic import SymbolicAgent
from divine_agents.box import Box, AgentWithBox


class TestSymbolicAgent(unittest.TestCase):
    def test_symbol_interpretation(self):
        agent = SymbolicAgent("sym", symbols=["\u2298", "\u222B"])
        agent.interpret_symbols()
        self.assertIn(
            "Resnica je absolutna in neodvisna od drugih.",
            agent.philosophical_beliefs,
        )
        self.assertIn(
            "Resnica je relativna, oblikovana skozi izku\u0161nje in odnose.",
            agent.philosophical_beliefs,
        )


class TestBox(unittest.TestCase):
    def test_box_influences_agent(self):
        agent = AgentWithBox("box-agent", tension=0.8)
        agent.add_task_to_box(
            "absolutna resnica: Resnica je nespremenljiva in neodvisna od kogarkoli."
        )
        agent.transition_with_box()
        self.assertIn(
            "Resnica je absolutna in neodvisna od drugih.",
            agent.philosophical_beliefs,
        )
        self.assertEqual(agent.state, "Jaz")


if __name__ == "__main__":
    unittest.main()
