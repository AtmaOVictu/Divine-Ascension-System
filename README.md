# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## File Watching

The system can record file modifications using the `Watcher` utility.

```python
from divine_agents.watch import Watcher
import time

watcher = Watcher("./")
watcher.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    watcher.stop()
```
