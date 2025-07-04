from __future__ import annotations
import json
from datetime import datetime
import urllib.request
from typing import Tuple


def get_local_time() -> str:
    """Return the current local time as an ISO formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_time_from_ip() -> Tuple[str, str, str]:
    """Return location, timezone and current time derived from the public IP."""
    with urllib.request.urlopen('https://ipinfo.io') as response:
        data = json.load(response)
    location = data.get('city', 'Unknown')
    timezone = data.get('timezone')
    if not timezone:
        raise ValueError('Timezone not found in IP information')
    with urllib.request.urlopen(f'http://worldtimeapi.org/api/timezone/{timezone}.json') as response:
        time_data = json.load(response)
    current_time = time_data['datetime']
    return location, timezone, current_time
