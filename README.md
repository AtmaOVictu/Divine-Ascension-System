# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Oracle Agent

The package now provides an ``OracleAgent`` that extends ``Agent`` with a
transition memory. It records each state change and can suggest the next step
based on its history. Example:

```python
from divine_agents import OracleAgent

oracle = OracleAgent("O")
oracle.update_tension(0.8)
oracle.transition()  # -> "Jaz"
print(oracle.transitions)
```
