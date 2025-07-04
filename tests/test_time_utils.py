import unittest
from unittest.mock import patch
from divine_agents import time_utils


class TestTimeUtils(unittest.TestCase):
    def test_current_local_time_format(self):
        t = time_utils.current_local_time()
        self.assertRegex(t, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

    def test_time_from_ip_fallback(self):
        if time_utils.requests is None:
            t = time_utils.time_from_ip()
            self.assertRegex(t, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")
        else:
            with patch('divine_agents.time_utils.requests.get') as mock_get:
                mock_get.side_effect = Exception('network error')
                t = time_utils.time_from_ip()
                self.assertRegex(t, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")


if __name__ == '__main__':
    unittest.main()
