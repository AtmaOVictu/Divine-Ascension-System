import unittest
from divine_agents.memory_agent import MemoryAgent

class TestMemoryAgent(unittest.TestCase):
    def test_memory_storage(self):
        agent = MemoryAgent("A")
        agent.remember("Veselje je kljucno.")
        self.assertEqual(len(agent.memory), 1)

    def test_sentiment_analysis(self):
        agent = MemoryAgent("A")
        agent.remember("Veselje je kljucno.")
        agent.remember("Cutim jeza.")
        sentiment = agent.analyze_sentiment()
        self.assertAlmostEqual(sentiment, 0.0, places=2)

    def test_response_influence(self):
        agent = MemoryAgent("A")
        agent.remember("Cutim jeza.")
        response = agent.respond_with_memory("Kaj je resnica?")
        self.assertIn("izzivov", response)

if __name__ == '__main__':
    unittest.main()
