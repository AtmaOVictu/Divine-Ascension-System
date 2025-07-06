import asyncio
import unittest

from divine_agents.agent import Agent
from divine_agents.async_dialogue import async_philosophical_debate


class TestAsyncDialogue(unittest.IsolatedAsyncioTestCase):
    async def test_async_debate_transitions(self):
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        lines = await async_philosophical_debate(a1, a2, rounds=2)
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)
        # Ensure transitions occurred due to emotion update
        self.assertIn('Jaz', a1.history + a2.history)
        self.assertTrue(any('resnica' in line.lower() for line in lines))


if __name__ == '__main__':
    unittest.main()


