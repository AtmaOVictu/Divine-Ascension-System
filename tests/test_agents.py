import unittest
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
        lines = philosophical_dialogue(a1, a2, rounds=1)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))

    def test_emotion_in_response(self):
        agent = Agent("A", emotion_label="strah")
        agent.update_emotion(0.6, label="strah")
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("(strah)"))

    def test_dialogue_causes_transition(self):
        a1 = Agent("B1")
        a2 = Agent("B2")
        philosophical_dialogue(a1, a2, rounds=2)
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)


if __name__ == '__main__':
    unittest.main()
