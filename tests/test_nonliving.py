import unittest
from divine_agents import NonLivingEntity, Agent, philosophical_dialogue


class TestNonLivingEntity(unittest.TestCase):
    def test_default_state(self):
        rock = NonLivingEntity("Stone", "Rock")
        self.assertEqual(rock.state, "Jaz")

    def test_describe_and_list(self):
        tree = NonLivingEntity("Tree", "Oak")
        water = NonLivingEntity("Water", "River")
        descriptions = NonLivingEntity.list_entities([tree, water])
        self.assertEqual(len(descriptions), 2)
        self.assertIn("Tree", descriptions[0])
        self.assertIn("Water", descriptions[1])

    def test_dialogue_integration(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        stone = NonLivingEntity("Stone", "Rock")
        lines = philosophical_dialogue(a1, a2, [stone])
        self.assertTrue(any("Stone" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
