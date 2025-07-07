import unittest
from divine_agents import Agent, Krak, CodexSystem, philosophical_dialogue


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


class TestKrak(unittest.TestCase):
    def test_krak_task_and_transition(self):
        k = Krak("K1")
        k.update_emotion(0.8)
        self.assertEqual(k.task, "high_emotion_task")
        state = k.transition()
        self.assertEqual(state, "Jaz")


class TestCodexSystem(unittest.TestCase):
    def test_system_updates(self):
        system = CodexSystem()
        a = Agent("A", tension=0.8)
        k = Krak("K1", tension=0.8)
        system.add_agent(a)
        system.add_krak(k)
        system.update()
        self.assertEqual(a.state, "Jaz")
        self.assertEqual(k.state, "Jaz")


if __name__ == '__main__':
    unittest.main()
