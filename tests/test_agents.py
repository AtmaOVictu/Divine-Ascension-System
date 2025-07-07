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
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
    def test_emotion_only_transition(self):
        agent = Agent("Emotional")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")
    def test_dialogue_full_output(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        expected = [
            "A1 (Ego): Resnica je absolutna in neodvisna od drugih.",
            "A2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.",
            "A1 prehaja v stanje: Jaz",
            "A2 prehaja v stanje: Enotnost",
            "A1: Resnica je relativna, oblikovana z našimi odnosi.",
            "A2: Vse resnice so eno, medsebojno povezane.",
        ]
        self.assertEqual(lines, expected)

    def test_normalized_boundaries(self):
        low = Agent("Low")
        low.update_tension(0.0)
        low.update_emotion(0.0)
        self.assertEqual(low.transition(), "Ego")

        high_tension = Agent("HighT")
        high_tension.update_tension(1.0)
        self.assertEqual(high_tension.transition(), "Jaz")

        high_emotion = Agent("HighE")
        high_emotion.update_tension(0.1)
        high_emotion.update_emotion(1.0)
        self.assertEqual(high_emotion.transition(), "Jaz")




if __name__ == '__main__':
    unittest.main()
