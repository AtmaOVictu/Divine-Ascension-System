import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.meta import MetaModule


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_trigger_transition(self):
        agent = Agent("B")
        agent.set_emotion("fear", 0.6)
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
        self.assertTrue(any("anger" in line or "joy" in line for line in lines))

    def test_meta_module_compare(self):
        meta = MetaModule()
        a1 = Agent("X", version="RES000")
        a2 = Agent("X", version="RES000")
        meta.add_agent(a1)
        meta.add_agent(a2)
        self.assertTrue(meta.compare_agents(a1, a2))


if __name__ == '__main__':
    unittest.main()
