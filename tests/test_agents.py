import unittest
from divine_agents.agent import Agent, AgentInstance
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.stance import Stance


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

    def test_instance_and_stance(self):
        stance = Stance("Moralni princip", "Odgovornost za vse odločitve")
        inst = AgentInstance("I1", weekly_level=3)
        self.assertEqual(inst.weekly_level, 3)
        stance_line = stance.apply(inst)
        self.assertIn("principu", stance_line)
        inst.update_tension(0.9)
        inst.transition()
        self.assertTrue(inst.state.startswith("tedenski nivo"))


if __name__ == '__main__':
    unittest.main()
