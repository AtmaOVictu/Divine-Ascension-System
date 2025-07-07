import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.batch_api import BatchManager
import json
import os


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

    def test_emotional_response(self):
        agent = Agent("B", emotion_name="jeza")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("jeza", reply)

    def test_batch_request_file(self):
        dialogues = ["Kaj je resnica?", "Kaj je smisel?"]
        manager = BatchManager(client=None)
        requests = manager.build_requests(dialogues)
        path = "test_batch.jsonl"
        manager.save_requests(requests, path)
        with open(path, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
        self.assertEqual(len(lines), 2)
        obj = json.loads(lines[0])
        self.assertEqual(obj["custom_id"], "request-1")
        os.remove(path)


if __name__ == '__main__':
    unittest.main()
