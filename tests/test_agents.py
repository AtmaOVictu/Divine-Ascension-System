import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.repl import run_demo_loop
import asyncio


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

    def test_emotion_triggers_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_influences_response(self):
        agent = Agent("C", emotion=0.8)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("emocionalno", reply)

    def test_run_demo_loop(self):
        agent = Agent("D")

        inputs = iter(["Kaj je resnica?", "quit"])
        outputs = []

        async def run_loop():
            await run_demo_loop(agent, input_func=lambda _: next(inputs), print_func=outputs.append)

        asyncio.run(run_loop())

        self.assertTrue(any("D (" in line for line in outputs))


if __name__ == '__main__':
    unittest.main()
