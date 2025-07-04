from __future__ import annotations

from datetime import datetime
from typing import Callable, Tuple
import json
from urllib.request import urlopen


def _default_get(url: str) -> dict:
    with urlopen(url) as resp:
        return json.loads(resp.read().decode())


def get_local_time() -> str:
    """Return the current local time formatted as a string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_time_from_ip(get_request: Callable[[str], dict] | None = None) -> Tuple[str, str, str]:
    """Return city, timezone and current time based on the client's IP address."""
    if get_request is None:
        get_request = _default_get

    info = get_request("https://ipinfo.io/json")
    timezone = info.get("timezone")
    city = info.get("city", "")

    time_data = get_request(f"http://worldtimeapi.org/api/timezone/{timezone}.json")
    current_time = time_data.get("datetime")
    return city, timezone, current_time
