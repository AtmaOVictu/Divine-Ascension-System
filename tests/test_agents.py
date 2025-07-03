import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.multi_interaction import multi_agent_debate


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
        self.assertTrue(any("(fear)" in line or "(joy)" in line for line in lines))

    def test_multi_debate(self):
        agents = [Agent("A1"), Agent("A2", state="Jaz")]
        transcript = multi_agent_debate(agents, rounds=2)
        self.assertTrue(any("Enotnost" in line for line in transcript))


if __name__ == '__main__':
    unittest.main()
