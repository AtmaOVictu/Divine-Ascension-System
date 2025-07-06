import unittest
from divine_agents.agent import Agent, ConflictAgent
from divine_agents.dialogue import philosophical_dialogue, debate_about_truth


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

    def test_conflict_agent(self):
        agent = ConflictAgent("B", conflict="moralna dilema")
        new_state = agent.choose_path()
        self.assertEqual(new_state, "Jaz")

    def test_debate_dialogue(self):
        a1 = Agent("X")
        a2 = Agent("Y", state="Jaz")
        lines = debate_about_truth(a1, a2)
        self.assertTrue(all(isinstance(line, str) for line in lines))


if __name__ == '__main__':
    unittest.main()
