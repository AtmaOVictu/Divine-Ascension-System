import unittest
from divine_agents import Agent, Environment, Word, philosophical_dialogue


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
        env = Environment("Test", {"social_pressure": 0.8})
        lines = philosophical_dialogue(a1, a2, env)
        self.assertTrue(any("truth" in line.lower() for line in lines))

    def test_environment_influence(self):
        agent = Agent("Env")
        env = Environment("E", {"moral_dilemma": 0.8})
        env.influence(agent)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")

    def test_word_definition(self):
        word = Word("truth")
        self.assertIn("synthesis", word.define())


if __name__ == '__main__':
    unittest.main()
