import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.connotation import categorize_words, Category


def test_categorize_words():
    result = categorize_words(["ljubezen", "strah", "ego"])
    assert Category.EMOTION in result
    assert "ljubezen" in result[Category.EMOTION]
    assert Category.STATE in result
    assert "ego" in result[Category.STATE]
