"""Utility functions for the divine agents package."""


def ionize_word(word: str) -> str:
    """Shift each character in *word* by one ASCII position.

    Parameters
    ----------
    word:
        Input word to transform.

    Returns
    -------
    str
        Transformed word.
    """
    return ''.join(chr(ord(c) + 1) for c in word)
