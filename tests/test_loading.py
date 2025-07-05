import unittest
from divine_agents.loading import LoadingScreenUnity


class TestLoadingScreenUnity(unittest.TestCase):
    def test_cycle_resets_unity(self):
        loader = LoadingScreenUnity("Test")
        reset = False
        prev = loader.unity_value
        for _ in range(200):
            loader.update_unity()
            if loader.unity_value < prev:
                reset = True
                break
            prev = loader.unity_value
        self.assertTrue(reset)


if __name__ == "__main__":
    unittest.main()
