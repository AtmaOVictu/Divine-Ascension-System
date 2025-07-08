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

class TestAdvancedAgents(unittest.TestCase):
    def test_emotion_based_transition(self):
        agent = Agent("E1")
        agent.update_emotion(0.6)
        new_state = agent.transition()
        self.assertEqual(new_state, "Jaz")

    def test_agent_dialogue(self):
        from divine_agents.figures import PhilosopherAgent, HeroAgent, agent_dialogue

        p = PhilosopherAgent("P")
        h = HeroAgent("H")
        convo = agent_dialogue(p, h)
        # After dialogue both should move at least one state forward
        self.assertIn(p.state, ("Jaz", "Enotnost"))
        self.assertIn(h.state, ("Jaz", "Enotnost"))
        self.assertTrue(any("Kaj je resnica" in line for line in convo))


if __name__ == "__main__":
    unittest.main()

