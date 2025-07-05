import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.interaction import Kapacitor, OkenskoSporocilo


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

    def test_emotion_trigger(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotional_response(self):
        agent = Agent("C", emotion=0.7)
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("Čutim močna čustva."))

    def test_kapacitor(self):
        k = Kapacitor()
        k.sprejmi_vhod("aktiviraj")
        self.assertEqual(k.state, "Aktivacija")
        self.assertGreater(k.intensity, 0)

    def test_okensko_sporocilo(self):
        captured = []

        def fake_input(prompt: str) -> str:
            captured.append(prompt)
            return "zaključi"

        o = OkenskoSporocilo("Test", input_func=fake_input)
        result = o.prikazi_okno()
        self.assertEqual(result, "zaključi")
        self.assertTrue(captured)


if __name__ == '__main__':
    unittest.main()
