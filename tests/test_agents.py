import unittest
from divine_agents.agent import Agent
from divine_agents.box import SpaceTimeBox
from divine_agents.dialogue import philosophical_dialogue


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

    def test_space_time_box(self):
        box = SpaceTimeBox(stage="∴")
        box.transition("∆", {"info": 1})
        state = box.get_state()
        self.assertEqual(state["stage"], "∆")
        self.assertEqual(state["time"], 1)

    def test_emotional_response(self):
        agent = Agent("Emo")
        agent.update_emotion(0.8)
        agent.transition()
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("strastjo", reply)


if __name__ == '__main__':
    unittest.main()
