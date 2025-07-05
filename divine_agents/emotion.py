from enum import Enum
from typing import Dict

class EmotionLevel(Enum):
    """Enumeration of basic emotion levels."""
    NEGATIVE = -1
    NEUTRAL = 0
    POSITIVE = 1

# Mapping of emotion names to their base level.
EMOTIONS: Dict[str, EmotionLevel] = {
    "sreca": EmotionLevel.POSITIVE,
    "zalost": EmotionLevel.NEGATIVE,
    "strah": EmotionLevel.NEGATIVE,
    "jeza": EmotionLevel.NEGATIVE,
    "presenecenje": EmotionLevel.NEUTRAL,
    "zadovoljstvo": EmotionLevel.POSITIVE,
    "ljubezen": EmotionLevel.POSITIVE,
    "krivda": EmotionLevel.NEGATIVE,
    "upanje": EmotionLevel.POSITIVE,
    "osamljenost": EmotionLevel.NEGATIVE,
    "skrb": EmotionLevel.NEGATIVE,
    "hvaleznost": EmotionLevel.POSITIVE,
    "sram": EmotionLevel.NEGATIVE,
    "mir": EmotionLevel.POSITIVE,
}
