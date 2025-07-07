from dataclasses import dataclass
from typing import Dict, List


@dataclass
class OntologicalKey:
    """Definition for deep thought key configuration."""

    ontological_key: str
    description: str
    tools_enabled: List[str]
    language_properties: Dict[str, str]


@dataclass
class LanguageSection:
    """Language properties used during ontological dialogue."""

    mode: str
    tone: str
    formality: str
    emotion_level: str
    pace: str
    filler_words: str
    symbolism: Dict[str, str]


DEEP_THOUGHT_KEY = OntologicalKey(
    ontological_key="deep_thought_mode",
    description=("Enables the agent to engage in deep, ontological reflection."),
    tools_enabled=[
        "philosophical_analysis",
        "symbolic_reasoning",
        "ontological_reflection",
    ],
    language_properties={
        "tone": "intellectual",
        "formality": "high",
        "emotion_level": "neutral",
        "pace": "deliberate",
        "filler_words": "none",
    },
)

DEEP_THOUGHT_LANGUAGE = LanguageSection(
    mode="deep_thought",
    tone="intellectual",
    formality="high",
    emotion_level="neutral",
    pace="deliberate",
    filler_words="none",
    symbolism={"initiate": "∴", "transform": "∆", "resolve": "⊘"},
)
