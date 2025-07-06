import os
import sys
import unittest

# Ensure project root is on the Python path so `divine_agents` can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_feel_updates_tension(self):
        agent = Agent("B")
        agent.feel(0.5)
        self.assertGreater(agent.tension, 0)
        self.assertEqual(agent.emotion, 0.5)

    def test_transition_by_emotion(self):
        agent = Agent("C")
        agent.feel(0.8)
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

    def test_dialogue_termination(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(
            lines[-1] in {
                "Eden od agentov je dosegel Enotnost.",
                "Dialog je končan brez dosega Enotnosti.",
            }
        )


if __name__ == '__main__':
    unittest.main()
