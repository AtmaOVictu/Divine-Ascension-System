import json
from typing import List, Dict, Any

try:
    from openai import OpenAI
except Exception:  # pragma: no cover - optional dependency
    OpenAI = None  # type: ignore


def create_batch_input(requests: List[Dict[str, Any]], path: str) -> None:
    """Write batch requests to a JSONL file."""
    with open(path, "w", encoding="utf-8") as fh:
        for req in requests:
            fh.write(json.dumps(req) + "\n")


def upload_batch_file(client: "OpenAI", path: str):
    """Upload batch input file to OpenAI if client is provided."""
    if client is None:
        raise RuntimeError("OpenAI client not available")
    return client.files.create(file=open(path, "rb"), purpose="batch")


def create_batch(client: "OpenAI", input_file_id: str, *, endpoint: str = "/v1/chat/completions", window: str = "24h"):
    """Create a batch job using the provided file ID."""
    if client is None:
        raise RuntimeError("OpenAI client not available")
    return client.batches.create(input_file_id=input_file_id, endpoint=endpoint, completion_window=window)
