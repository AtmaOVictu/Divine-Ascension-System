"""Configuration for ontological modes and language settings."""

DEEP_THOUGHT_CONFIG = {
    "ontological_key": "deep_thought_mode",
    "description": (
        "Enables the agent to engage in deep, ontological reflection. "
        "This mode ensures the agent uses ontologically driven tools and follows symbolic transformations."
    ),
    "tools_enabled": [
        "philosophical_analysis",
        "symbolic_reasoning",
        "ontological_reflection",
    ],
    "language_properties": {
        "tone": "intellectual",
        "formality": "high",
        "emotion_level": "neutral",
        "pace": "deliberate",
        "filler_words": "none",
        "symbolism": {
            "initiate": "∴",
            "transform": "∆",
            "resolve": "⊘",
        },
    },
}
