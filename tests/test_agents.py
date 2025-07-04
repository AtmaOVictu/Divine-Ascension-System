import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_express_emotion_triggers_transition(self):
        agent = Agent("B", tension=0.3)
        agent.express_emotion("anger", 0.6)
        self.assertEqual(agent.state, "Jaz")

    def test_responses_include_prefix(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("Čustveno") or reply.startswith("Strastno"))

    def test_dialogue_contains_transitions(self):
        a1 = Agent("A1", tension=0.3)
        a2 = Agent("A2", state="Jaz", tension=0.4)
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
