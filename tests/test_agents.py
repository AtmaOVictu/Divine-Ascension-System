import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
import tempfile
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

    def test_logging(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            log_path = tmp.name
        try:
            agent.transition(log_path)
            with open(log_path, "r", encoding="utf-8") as f:
                data = f.read()
            self.assertIn(agent.state, data)
        finally:
            os.remove(log_path)


if __name__ == '__main__':
    unittest.main()
