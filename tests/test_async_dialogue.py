import os
import sys
import asyncio
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.async_dialogue import asynchronous_dialogue


class TestAsyncDialogue(unittest.IsolatedAsyncioTestCase):
    async def test_async_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        await asynchronous_dialogue(a1, a2, increments1=[0.8], increments2=[0.8])
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")


if __name__ == "__main__":
    asyncio.run(unittest.main())
