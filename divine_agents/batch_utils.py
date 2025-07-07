"""Helper utilities for creating OpenAI Batch API jobs."""

from __future__ import annotations

import json
from typing import Iterable

try:
    from openai import OpenAI
except Exception:  # pragma: no cover - optional dependency
    OpenAI = None  # type: ignore


def create_batch_jsonl(requests: Iterable[dict], file_path: str) -> None:
    """Write a JSONL file compatible with the OpenAI Batch API."""
    with open(file_path, "w", encoding="utf-8") as f:
        for i, body in enumerate(requests, start=1):
            payload = {
                "custom_id": f"request-{i}",
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": body,
            }
            f.write(json.dumps(payload) + "\n")


def submit_batch(file_path: str, completion_window: str = "24h") -> object:
    """Submit a batch job. Requires ``openai`` package and credentials."""
    if OpenAI is None:
        raise ImportError("openai package is required to submit batches")

    client = OpenAI()
    uploaded = client.files.create(file=open(file_path, "rb"), purpose="batch")
    batch = client.batches.create(
        input_file_id=uploaded.id,
        endpoint="/v1/chat/completions",
        completion_window=completion_window,
    )
    return batch
