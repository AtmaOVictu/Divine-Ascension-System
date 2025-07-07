import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.wide_agent import WideAgent
from divine_agents.narrow_agent import NarrowAgent
from divine_agents.system import ComplexSystem


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


class TestWideNarrowAgents(unittest.TestCase):
    def test_wide_agent_transition(self):
        agent = WideAgent("WA")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_narrow_agent_update(self):
        agent = NarrowAgent("NA")
        agent.update_value(0.8)
        self.assertEqual(agent.state, "Jaz")

    def test_system_process(self):
        system = ComplexSystem()
        lines = system.process()
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
