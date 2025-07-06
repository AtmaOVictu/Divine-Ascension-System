import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.instrumentation import DataHarvester, CodeLogger, CodeInterpreter


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_below_threshold(self):
        agent = Agent("B")
        agent.update_tension(0.3)
        agent.update_emotion(0.2)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_instrumentation(self):
        agent = Agent("C")
        harvester = DataHarvester()
        logger = CodeLogger()
        interpreter = CodeInterpreter(agent)

        harvester.collect_data({'tension': 0.9})
        state = interpreter.interpret_decision({'tension': 0.9})
        logger.log_event(state)

        self.assertEqual(state, "Jaz")
        self.assertIn(state, logger.history)


if __name__ == '__main__':
    unittest.main()
