import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_based_on_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertEqual(agent.history, ["Ego", "Jaz"])

    def test_history_logs_states(self):
        agent = Agent("C")
        agent.update_tension(0.8)
        agent.transition()
        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.history, ["Ego", "Jaz", "Enotnost"])

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertIn("A1 prehaja v stanje: Jaz", lines)
        self.assertIn("A2 prehaja v stanje: Enotnost", lines)
        self.assertEqual(lines[-2], "A1: Resnica je relativna, oblikovana z našimi odnosi.")
        self.assertEqual(lines[-1], "A2: Vse resnice so eno, medsebojno povezane.")


if __name__ == '__main__':
    unittest.main()
