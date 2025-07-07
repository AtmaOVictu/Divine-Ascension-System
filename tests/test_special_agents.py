import unittest
from divine_agents.special_agents import (
    RespectAgent,
    DisrespectAgent,
    FearAgent,
    OneValueAgent,
)


class TestSpecialAgents(unittest.TestCase):
    def test_respect_agent_response(self):
        agent = RespectAgent("R")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("Spoštovanje", reply)

    def test_disrespect_agent_response(self):
        agent = DisrespectAgent("D")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("iluzija", reply)

    def test_fear_agent_transition(self):
        agent = FearAgent("F")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_one_value_agent_response(self):
        agent = OneValueAgent("O", value=0.3)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("Ne vidim", reply)


if __name__ == '__main__':
    unittest.main()
