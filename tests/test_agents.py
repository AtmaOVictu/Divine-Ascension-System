import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, opposite_necessity
from divine_agents.nano_mega import NanoMoment, MegaMoment


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

    def test_opposite_necessity(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        opposite_necessity(a1, a2)
        self.assertGreater(a1.tension, 0.0)
        self.assertGreater(a2.tension, 0.0)

    def test_nano_mega_transition(self):
        agent = Agent("A")
        nano = NanoMoment(0.9)
        mega = MegaMoment(threshold=0.9)
        nano.apply(agent)
        mega.accumulate(nano)
        mega.trigger(agent)
        self.assertEqual(agent.state, "Jaz")


if __name__ == '__main__':
    unittest.main()
