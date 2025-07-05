import unittest
from divine_agents import Agent, philosophical_dialogue, Conversation


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

    def test_conversation_run(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        convo = Conversation(a1, a2)
        history = convo.run(steps=2)
        self.assertEqual(len(history), 8)
        # After enough steps, at least one agent should reach Enotnost
        self.assertIn("Enotnost", " ".join(history))


if __name__ == "__main__":
    unittest.main()
