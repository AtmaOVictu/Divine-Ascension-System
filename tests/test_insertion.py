import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.insertion import InsertionAgent
from divine_agents.dialogue import dynamic_dialogue


class TestInsertionAgent(unittest.TestCase):
    def test_insert_state(self):
        agent = Agent("A")
        insert = InsertionAgent(agent)
        insert.insert_state("Transcendence")
        self.assertIn("Transcendence", Agent.STATES)

    def test_dynamic_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dynamic_dialogue(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
