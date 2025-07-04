import unittest
import os
import sys
import json
from unittest import mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.time_utils import get_local_time, get_time_from_ip


class TestTimeUtils(unittest.TestCase):
    def test_get_local_time_format(self):
        time_str = get_local_time()
        self.assertRegex(time_str, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

    def test_get_time_from_ip_mocked(self):
        fake_ipinfo = json.dumps({'city': 'TestCity', 'timezone': 'Europe/Ljubljana'}).encode()
        fake_time = json.dumps({'datetime': '2024-01-01T00:00:00+00:00'}).encode()

        def fake_urlopen(url):
            class FakeResponse:
                def __init__(self, data):
                    self._data = data
                def __enter__(self):
                    from io import BytesIO
                    self._io = BytesIO(self._data)
                    return self._io
                def __exit__(self, exc_type, exc, tb):
                    self._io.close()
            if 'ipinfo.io' in url:
                return FakeResponse(fake_ipinfo)
            return FakeResponse(fake_time)

        with mock.patch('urllib.request.urlopen', fake_urlopen):
            location, tz, time_str = get_time_from_ip()
        self.assertEqual(location, 'TestCity')
        self.assertEqual(tz, 'Europe/Ljubljana')
        self.assertEqual(time_str, '2024-01-01T00:00:00+00:00')


if __name__ == '__main__':
    unittest.main()
