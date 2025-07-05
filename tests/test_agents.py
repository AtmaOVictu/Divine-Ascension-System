import unittest
import os
import sys
import time

# Ensure the project root is on the Python path when tests are executed from
# different working directories.
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


def simulate_loading_screen(agent_name: str, max_cycles: int = 5):
    """Simulate progress updates for a loading screen."""
    progress = []
    agent = Agent(agent_name)
    for cycle in range(max_cycles):
        progress.append(f"Loading: {cycle + 1}/{max_cycles} - {agent.name}")
        time.sleep(0.01)
    progress.append(f"Loading Screen končan za {agent.name}.")
    return progress


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

    def test_loading_screen(self):
        progress = simulate_loading_screen("Agent1", max_cycles=3)
        self.assertTrue(progress[-1].startswith("Loading Screen končan"))


if __name__ == '__main__':
    unittest.main()
