import unittest
from divine_agents.agent import Agent, AgentWithConflict
from divine_agents.dialogue import philosophical_dialogue, philosophical_debate


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

    def test_conflict_choice(self):
        ag = AgentWithConflict("B", conflict="moralna dilema")
        new_state = ag.choose_path()
        self.assertEqual(new_state, "Jaz")

    def test_debate(self):
        ag1 = Agent("C1")
        ag2 = Agent("C2", state="Jaz")
        conv = philosophical_debate(ag1, ag2)
        self.assertTrue(any("custvom" in line for line in conv))


if __name__ == '__main__':
    unittest.main()
