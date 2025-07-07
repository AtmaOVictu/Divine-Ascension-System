from typing import Dict

# Default transition matrix with probabilities for state changes.
# Rows correspond to current state and columns to next state.
# States: Ego, Jaz, Enotnost
DEFAULT_MATRIX: Dict[str, Dict[str, float]] = {
    "Ego": {"Ego": 0.6, "Jaz": 0.3, "Enotnost": 0.1},
    "Jaz": {"Ego": 0.2, "Jaz": 0.5, "Enotnost": 0.3},
    "Enotnost": {"Ego": 0.0, "Jaz": 0.4, "Enotnost": 0.6},
}
