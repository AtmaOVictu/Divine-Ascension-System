"""Utilities for interacting with OpenAI's Batch API."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List
import json
import tempfile

from openai import OpenAI


@dataclass
class BatchRequest:
    custom_id: str
    system_prompt: str
    user_prompt: str
    max_tokens: int = 150

    def to_json(self) -> str:
        body = {
            "model": "gpt-4",
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.user_prompt},
            ],
            "max_tokens": self.max_tokens,
        }
        request = {
            "custom_id": self.custom_id,
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": body,
        }
        return json.dumps(request)


def create_batch_file(requests: Iterable[BatchRequest]) -> str:
    """Create a temporary jsonl file for batch processing."""
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".jsonl")
    with open(tmp.name, "w", encoding="utf-8") as fh:
        for req in requests:
            fh.write(req.to_json() + "\n")
    return tmp.name


def submit_batch(request_file: str, completion_window: str = "24h") -> str:
    """Upload a batch file and create a batch job. Returns batch id."""
    client = OpenAI()
    file_obj = client.files.create(file=open(request_file, "rb"), purpose="batch")
    batch = client.batches.create(
        input_file_id=file_obj.id,
        endpoint="/v1/chat/completions",
        completion_window=completion_window,
    )
    return batch.id
