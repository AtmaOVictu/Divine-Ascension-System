from datetime import datetime
from typing import Optional

try:
    import requests  # type: ignore
except ImportError:  # pragma: no cover - environment without requests
    requests = None


def current_local_time() -> str:
    """Return current local time as an ISO formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def time_from_ip() -> str:
    """Return current time based on timezone from local IP.

    This function tries to use external services to determine the timezone.
    If the requests library is unavailable or a network error occurs, it
    falls back to the local system time.
    """
    if not requests:
        return current_local_time()
    try:
        info = requests.get("https://ipinfo.io/json", timeout=5)
        tz: Optional[str] = info.json().get("timezone")
        if not tz:
            raise ValueError("timezone not found")
        world_time = requests.get(
            f"http://worldtimeapi.org/api/timezone/{tz}", timeout=5
        )
        return world_time.json().get("datetime")
    except Exception:
        return current_local_time()
