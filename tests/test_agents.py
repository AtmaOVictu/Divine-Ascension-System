import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.semantics import VectorStore


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
        self.assertTrue(any(line.startswith("[spomin]") for line in lines))

    def test_semantic_search(self):
        store = VectorStore()
        texts = [
            "Resnica je absolutna.",
            "Resnica je relativna.",
            "Vse resnice so eno."
        ]
        store.add_texts(texts)
        result = store.search("relativna resnica", top_k=1)
        self.assertEqual(result[0], "Resnica je relativna.")


if __name__ == '__main__':
    unittest.main()
