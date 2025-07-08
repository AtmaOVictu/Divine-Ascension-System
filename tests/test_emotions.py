import unittest
from divine_agents.emotions import Emotion, Karma, track_emotional_trends


class TestEmotions(unittest.TestCase):
    def test_karma_negative_from_anger(self):
        emotion = Emotion(anger=0.9)
        karma = Karma()
        karma.update(emotion, 0.0)
        self.assertLess(karma.karma_value, 0)

    def test_track_trends_length(self):
        emotions_series = [Emotion(joy=0.5), Emotion(anger=0.6)]
        trends = track_emotional_trends(emotions_series, iterations=5)
        self.assertEqual(len(trends['joy'][0]), 5)
        self.assertEqual(len(trends['karma'][0]), 5)


if __name__ == '__main__':
    unittest.main()
