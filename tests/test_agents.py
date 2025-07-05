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
        agent = Agent("A", state="Ego")
        self.assertEqual(
            agent.respond("Kaj je resnica?"),
            "Resnica je absolutna in neodvisna od drugih."
        )

        agent.state = "Jaz"
        self.assertEqual(
            agent.respond("Kaj je resnica?"),
            "Resnica je relativna, oblikovana z našimi odnosi."
        )

        agent.state = "Enotnost"
        self.assertEqual(
            agent.respond("Kaj je resnica?"),
            "Vse resnice so eno, medsebojno povezane."
        )

    def test_emotion_triggers_transition(self):
        agent = Agent("A")
        agent.update_tension(0.1)  # ensure low tension
        agent.update_emotion(0.6)  # high emotion should trigger transition
        agent.update_tension(0.1)  # keep tension below threshold
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
