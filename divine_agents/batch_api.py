"""Utilities for interacting with OpenAI's Batch API."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from openai import OpenAI


class BatchAPI:
    """Wrapper around the OpenAI Batch API for asynchronous tasks."""

    def __init__(self, client: Optional[OpenAI] = None) -> None:
        self.client = client or OpenAI()

    def upload_file(self, path: Path):
        """Upload a JSONL file to be used for batch processing."""
        return self.client.files.create(file=open(path, "rb"), purpose="batch")

    def create_batch(self, input_file_id: str, endpoint: str = "/v1/chat/completions", *, completion_window: str = "24h"):
        """Create a batch job from a previously uploaded file."""
        return self.client.batches.create(
            input_file_id=input_file_id,
            endpoint=endpoint,
            completion_window=completion_window,
        )

    def status(self, batch_id: str):
        """Retrieve the status of an existing batch."""
        return self.client.batches.retrieve(batch_id)

    def cancel(self, batch_id: str):
        """Cancel an in-progress batch."""
        return self.client.batches.cancel(batch_id)

    def get_results(self, file_id: str) -> str:
        """Return the textual content of a result or error file."""
        return self.client.files.content(file_id).text
