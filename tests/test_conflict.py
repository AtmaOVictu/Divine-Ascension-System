import unittest
from divine_agents import Agent, OntologicalConflict


class TestConflict(unittest.TestCase):
    def test_nasprotje_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        conflict = OntologicalConflict(a1, a2)
        for _ in range(6):
            conflict.increase_conflict(0.1)
        lines = conflict.step()
        self.assertIn('Nasprotje', a1.state)
        self.assertIn('Nasprotje', a2.state)
        self.assertTrue(any('nasprotja' in line.lower() for line in lines))

    def test_emotional_response(self):
        agent = Agent("A", state="Jaz")
        agent.update_emotion(0.8)
        resp = agent.respond('Kaj je resnica?')
        self.assertIn('Močno', resp)


if __name__ == '__main__':
    unittest.main()
