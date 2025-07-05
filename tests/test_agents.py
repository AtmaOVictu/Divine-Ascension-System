import unittest
import sys
from pathlib import Path

# Ensure project root is in the path for imports when tests are executed
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


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

    def test_json_persistence(self):
        agent = Agent("Persist", state="Jaz")
        agent.update_emotion(0.8)
        agent.transition()
        tmp = Path("agent_tmp.json")
        try:
            agent.save(tmp)
            loaded = Agent.load(tmp)
            self.assertEqual(agent.state, loaded.state)
            self.assertEqual(agent.history, loaded.history)
        finally:
            if tmp.exists():
                tmp.unlink()


if __name__ == '__main__':
    unittest.main()
