import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.boxing_station import BoxingStation, Bit


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


class TestBoxingStation(unittest.TestCase):
    def test_agent_interaction_creates_box(self):
        bs = BoxingStation()
        a1 = Agent("A1", state="Ego")
        a2 = Agent("A2", state="Jaz")
        bs.interaction(a1, a2)
        self.assertIn("Self-Other Reflection Box", bs.boxes)

    def test_bit_interaction_creates_box(self):
        bs = BoxingStation()
        b1 = Bit(0)
        b2 = Bit(1)
        bs.interaction(b1, b2)
        self.assertIn("Bit Interaction Box", bs.boxes)


if __name__ == '__main__':
    unittest.main()
