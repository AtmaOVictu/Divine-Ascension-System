"""Utility for creating simple ontological rhythms."""
from typing import List

_PHONEMES = {
    "Ego": ["E", "G", "O"],
    "Jaz": ["J", "A", "Z"],
    "Enotnost": ["E", "N", "O", "T", "N", "O"],
}

def create_rhythm(states: List[str]) -> List[str]:
    """Return a sequence of phoneme strings representing a rhythm."""
    rhythm = []
    for state in states:
        phonemes = _PHONEMES.get(state, [])
        rhythm.append("-".join(phonemes))
    return rhythm
