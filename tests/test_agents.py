import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, dynamic_dialogue


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

    def test_dynamic_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        log = dynamic_dialogue(a1, a2, rounds=2)
        self.assertTrue(a1.state in {"Jaz", "Enotnost"})
        self.assertTrue(any("prehaja" in line for line in log))

    def test_emotional_response(self):
        agent = Agent("B", emotion=0.6, emotion_type="strah")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("strah", reply)


if __name__ == '__main__':
    unittest.main()
