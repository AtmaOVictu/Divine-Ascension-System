from dataclasses import dataclass
from typing import List, Dict

@dataclass
class OntologicalKey:
    ontological_key: str
    description: str
    tools_enabled: List[str]
    language_properties: Dict[str, str]


@dataclass
class LanguageSection:
    mode: str
    tone: str
    formality: str
    emotion_level: str
    pace: str
    filler_words: str
    symbolism: Dict[str, str]


deep_thought_key = OntologicalKey(
    ontological_key="deep_thought_mode",
    description=(
        "Enables the agent to engage in deep, ontological reflection. "
        "This key ensures that the agent uses ontologically-driven tools "
        "and follows symbolic transformations (∴, ∆, ⊘)."
    ),
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


deep_thought_language = LanguageSection(
    mode="deep_thought",
    tone="intellectual",
    formality="high",
    emotion_level="neutral",
    pace="deliberate",
    filler_words="none",
    symbolism={"initiate": "∴", "transform": "∆", "resolve": "⊘"},
)
