import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.metaparadox import MetaparadoxicalModule
from divine_agents.relative_absolutes import RelativeAbsoluteLibrary


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
        # Ensure at least one transition occurs
        self.assertTrue(any("->" in line for line in lines))

    def test_metaparadoxical_transition(self):
        a = Agent("M")
        a.update_emotion(0.6)
        meta = MetaparadoxicalModule(a)
        meta.paradoxical_transition()
        self.assertEqual(a.state, "Jaz")

    def test_relative_absolute_library(self):
        lib = RelativeAbsoluteLibrary()
        lib.set_absolute("truth", 1.0)
        val = lib.get_absolute("truth")
        self.assertGreater(val, 0.5)


if __name__ == '__main__':
    unittest.main()
