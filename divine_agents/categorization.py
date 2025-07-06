"""Utility functions for categorizing terms based on simple connotations."""

from collections import defaultdict
from typing import Dict, Iterable, List


CONNOTATION_MAP = {
    "fear": "emotion",
    "joy": "emotion",
    "anger": "emotion",
    "Ego": "state",
    "Jaz": "state",
    "Enotnost": "state",
}


def categorize_terms(terms: Iterable[str]) -> Dict[str, List[str]]:
    """Categorize given terms into groups defined in ``CONNOTATION_MAP``.

    Unknown terms are grouped under the ``concept`` category.
    """
    categories: Dict[str, List[str]] = defaultdict(list)
    for term in terms:
        category = CONNOTATION_MAP.get(term, "concept")
        categories[category].append(term)
    return dict(categories)
