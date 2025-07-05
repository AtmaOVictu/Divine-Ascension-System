import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents import agent_precheck, command_filter


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

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_emotions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, emotion1="strah", intensity1=0.4, emotion2="jeza", intensity2=0.8)
        self.assertTrue(any("\u010dutim" in line for line in lines))

    def test_agent_precheck_and_filter(self):
        agent = Agent("C")
        agent.update_tension(0.9)
        msg = agent_precheck(agent, "prehod")
        self.assertIn("potrebuje obravnavo", msg)
        filtered = command_filter(agent, "prehod")
        self.assertEqual(filtered, msg)
        response = command_filter(agent, "respond")
        self.assertIn("Resnica", response)


if __name__ == '__main__':
    unittest.main()
