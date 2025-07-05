# Divine-Ascension-System

This project simulates ontological agents that transition between three
philosophical states: **Ego**, **Jaz**, and **Enotnost**. Agents change state
when their tension or emotion levels exceed specific thresholds. Each
transition is validated through a *legitimator* which ensures that the
transition abides by the ontological rules defined in `Agent.is_legitimate_transition`.

Unit tests covering these behaviours can be run with:

```bash
pytest -q
```
