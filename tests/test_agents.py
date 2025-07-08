import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.retrieval import VectorStore


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
        store = VectorStore()
        lines = philosophical_dialogue(a1, a2, store=store)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # ensure something was stored and can be retrieved
        results = store.search("resnica", top_k=1)
        self.assertTrue(results)


class TestSemanticSearch(unittest.TestCase):
    def test_search(self):
        store = VectorStore()
        store.add("Resnica je absolutna in neodvisna od drugih.")
        store.add("Resnica je relativna, oblikovana z našimi odnosi.")
        results = store.search("absolutna resnica", top_k=1)
        self.assertIn("absolutna", results[0])


if __name__ == '__main__':
    unittest.main()
