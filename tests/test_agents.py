import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.tension = 0.8
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

    def test_moral_decision_loyal(self):
        agent = Agent("B", loyalty=0.8, emotional_state="fearful")
        decision = agent.make_moral_decision("situation")
        self.assertIn("help others", decision)

    def test_collaborative_task_success(self):
        member1 = Agent("M1", loyalty=0.9, emotional_state="happy")
        member2 = Agent("M2", loyalty=0.9, emotional_state="happy")
        leader = Agent("L", loyalty=0.9, team=[member1, member2])
        result = leader.collaborative_task()
        self.assertIn("successfully", result)


if __name__ == '__main__':
    unittest.main()
