import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_when_below_thresholds(self):
        agent = Agent("A")
        state_before = agent.state
        state_after = agent.transition()
        self.assertEqual(state_before, state_after)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_transition_via_emotion(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_history_records_states(self):
        agent = Agent("A")
        agent.transition()  # remains Ego
        agent.update_emotion(0.6)
        agent.transition()  # Ego -> Jaz
        agent.update_emotion(0.8)
        agent.transition()  # Jaz -> Enotnost
        self.assertEqual(agent.history, ["Ego", "Ego", "Jaz", "Enotnost"])


if __name__ == '__main__':
    unittest.main()
