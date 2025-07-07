# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Batch API Integration

The project includes `divine_agents.batch_api.BatchAPI` which wraps the OpenAI
Batch API. It can upload JSONL request files, create batches for asynchronous
processing and retrieve results once the batch finishes. Batches are useful for
running large numbers of philosophical dialogues or evaluations without waiting
for immediate responses.

Example usage:

```python
from divine_agents import BatchAPI
api = BatchAPI()
file = api.upload_file("batchinput.jsonl")
batch = api.create_batch(file.id)
print(api.status(batch.id))
```
