import unittest
from divine_agents.agent import Agent
from divine_agents.meditation import Mediator, Meditacija, Transformacija


class TestMeditationAndMediation(unittest.TestCase):
    def test_meditacija_triggers_transition(self):
        agent = Agent("A")
        med = Meditacija(agent)
        new_state = med.reflect()
        self.assertEqual(new_state, "Jaz")

    def test_mediator_triggers_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        mediator = Mediator("M")
        state = mediator.mediate(a1, a2)
        self.assertEqual(state, "Jaz")

    def test_transformacija(self):
        agent = Agent("T", state="Jaz")
        trans = Transformacija(agent)
        new_state = trans.transform()
        self.assertEqual(new_state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
