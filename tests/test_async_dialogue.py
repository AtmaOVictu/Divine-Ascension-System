import asyncio
import unittest

from divine_agents.agent import Agent
from divine_agents.async_dialogue import async_philosophical_dialogue


class TestAsyncDialogue(unittest.TestCase):
    def test_async_dialogue_transitions(self):
        a1 = Agent('A1', tension=0.8)
        a2 = Agent('A2', tension=0.8)
        lines = asyncio.run(async_philosophical_dialogue(a1, a2, steps=1))
        self.assertTrue(any('A1' in line for line in lines))
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)
        self.assertGreaterEqual(len(lines), 2)


if __name__ == '__main__':
    unittest.main()
