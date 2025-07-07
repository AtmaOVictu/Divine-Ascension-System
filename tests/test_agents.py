import unittest
import json
import os

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.batch_api import create_batch_input


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", emotion_label="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("joy", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_batch_file_creation(self):
        requests = [
            {
                "custom_id": "1",
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": {"model": "gpt-4", "messages": [{"role": "user", "content": "test"}]},
            }
        ]
        path = "tests/tmp_batch.jsonl"
        create_batch_input(requests, path)
        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        os.remove(path)
        self.assertEqual(len(lines), 1)
        self.assertEqual(json.loads(lines[0])["custom_id"], "1")


if __name__ == '__main__':
    unittest.main()
