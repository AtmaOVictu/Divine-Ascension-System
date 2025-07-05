from typing import List

# Key words describing phases of tension
KEYWORDS = [
    "Zagon",
    "Akumulacija",
    "Omejitev",
    "Razpad",
    "Reakcija",
    "Refleksija",
    "Prehod",
    "Energija",
    "Harmoničnost",
    "Zavrnitev",
]


def tension_keywords() -> List[str]:
    """Return the key words that define stages of tension."""
    return KEYWORDS


def tension_stage(tension: float) -> str:
    """Return a keyword representing the stage of the given tension level."""
    if tension < 0.1:
        return "Zagon"
    if tension < 0.3:
        return "Akumulacija"
    if tension < 0.7:
        return "Omejitev"
    if tension < 1.0:
        return "Reakcija"
    return "Razpad"
