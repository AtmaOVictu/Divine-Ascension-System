NOTES = ["C", "D", "E", "F", "G", "A", "B"]


def generate_scale(root: str, length: int = 7) -> list[str]:
    """Generate a simple major scale starting from ``root``."""
    if root not in NOTES:
        raise ValueError("Unknown root note")
    start = NOTES.index(root)
    scale = []
    for i in range(length):
        scale.append(NOTES[(start + i) % len(NOTES)])
    return scale
