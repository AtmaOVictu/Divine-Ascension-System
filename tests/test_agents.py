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

class TestDigitalTranscendence(unittest.TestCase):
    def test_transcendence_success(self):
        agent = Agent("T", tension=1.0, emotion=1.0)
        from divine_agents.transcendence import initiate_agent_digital_transcendence
        result = initiate_agent_digital_transcendence(agent)
        self.assertTrue(result)
        self.assertEqual(agent.state, "Enotnost")

    def test_transcendence_failure(self):
        agent = Agent("T", tension=0.4, emotion=0.4)
        from divine_agents.transcendence import initiate_agent_digital_transcendence
        result = initiate_agent_digital_transcendence(agent)
        self.assertFalse(result)
        self.assertNotEqual(agent.state, "Enotnost")

if __name__ == "__main__":
    unittest.main()
