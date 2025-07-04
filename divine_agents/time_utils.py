"""Utility functions for retrieving absolute time information."""

from datetime import datetime
from typing import Tuple

try:
    import requests
except Exception:  # pragma: no cover - requests might not be available
    requests = None


def get_local_time() -> str:
    """Return current local time as an ISO formatted string."""
    return datetime.now().isoformat()


def get_time_from_ip() -> Tuple[str, str, str]:
    """Return location, timezone and current time determined via IP address.

    Falls back to local time if network access is unavailable.
    """
    if requests is None:
        return "Unknown", "Local", get_local_time()

    try:
        info = requests.get("https://ipinfo.io", timeout=5)
        data = info.json()
        city = data.get("city", "Unknown")
        zone = data.get("timezone", "Local")
        time_resp = requests.get(f"http://worldtimeapi.org/api/timezone/{zone}.json", timeout=5)
        time_data = time_resp.json()
        current = time_data.get("datetime", get_local_time())
        return city, zone, current
    except Exception:
        return "Unknown", "Local", get_local_time()
