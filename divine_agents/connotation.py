from enum import Enum, auto
from typing import Dict, List


class Category(Enum):
    EMOTION = auto()
    STATE = auto()
    CONCEPT = auto()


# Mapping words to (connotation, category)
_CONNOTATIONS: Dict[str, Category] = {
    "ljubezen": Category.EMOTION,
    "strah": Category.EMOTION,
    "jaz": Category.STATE,
    "ego": Category.STATE,
    "enotnost": Category.CONCEPT,
}


def categorize_words(words: List[str]) -> Dict[Category, List[str]]:
    """Return a mapping of categories to the words that belong to them."""
    categories: Dict[Category, List[str]] = {}
    for word in words:
        category = _CONNOTATIONS.get(word.lower())
        if category:
            categories.setdefault(category, []).append(word)
    return categories


__all__ = ["Category", "categorize_words"]
