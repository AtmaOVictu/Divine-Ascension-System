import unittest
from divine_agents.nasprotje_iskalec import NasprotjeIskalec


class TestNasprotjeIskalec(unittest.TestCase):
    def test_find_missing_opposites(self):
        agent = NasprotjeIskalec("Iskalec")
        result = agent.find_missing_opposites("empty_space")
        self.assertIn("praznina", result)
        self.assertIn("Nasprotje ni prisotno", agent.missing_opposites)

    def test_transition_on_missing_opposites(self):
        agent = NasprotjeIskalec("Iskalec")
        agent.find_missing_opposites("empty_space")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_respond(self):
        agent = NasprotjeIskalec("Iskalec", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("zdruzene", reply)


if __name__ == "__main__":
    unittest.main()
