import unittest

from divine_agents.agent import Agent
from divine_agents.environment import Environment, timed_dialogue


class TestEnvironment(unittest.TestCase):
    def test_environment_time_advances(self):
        env = Environment()
        before = env.now()
        # perform some operations
        _ = timed_dialogue(Agent('A'), Agent('B'), env)
        after = env.now()
        self.assertGreater(after, before)

    def test_timed_dialogue_contains_timestamps(self):
        env = Environment()
        lines = timed_dialogue(Agent('A'), Agent('B', state='Jaz'), env)
        self.assertTrue(all(line.startswith('[') and 's]' in line for line in lines))


if __name__ == '__main__':
    unittest.main()
