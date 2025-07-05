import unittest

from divine_agents.agent import Agent
from divine_agents.multi_dialogue import vecstranska_razprava


class TestVecstranskaRazprava(unittest.TestCase):
    def test_vec_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        a3 = Agent("A3", state="Enotnost")
        lines = vecstranska_razprava([a1, a2, a3])
        self.assertTrue(any("preha" in line for line in lines))
        self.assertTrue(a1.state in Agent.STATES)
        self.assertTrue(a2.state in Agent.STATES)
        self.assertTrue(a3.state in Agent.STATES)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
