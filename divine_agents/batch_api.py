"""Utilities for creating and submitting OpenAI Batch API jobs."""

from __future__ import annotations

import json
from typing import List, Dict, Iterable

try:
    from openai import OpenAI
except ImportError:  # pragma: no cover - handled in tests
    OpenAI = None  # type: ignore


class BatchManager:
    """Manage batch requests for processing philosophical dialogues."""

    def __init__(self, client: OpenAI | None = None) -> None:
        self.client = client or (OpenAI() if OpenAI else None)

    @staticmethod
    def build_requests(dialogues: Iterable[str]) -> List[Dict]:
        """Create request objects suitable for OpenAI Batch API."""
        requests = []
        for i, message in enumerate(dialogues, 1):
            requests.append(
                {
                    "custom_id": f"request-{i}",
                    "method": "POST",
                    "url": "/v1/chat/completions",
                    "body": {
                        "model": "gpt-4",
                        "messages": [
                            {
                                "role": "system",
                                "content": "You are an agent in a philosophical dialogue.",
                            },
                            {"role": "user", "content": message},
                        ],
                        "max_tokens": 150,
                    },
                }
            )
        return requests

    @staticmethod
    def save_requests(requests: Iterable[Dict], path: str) -> None:
        """Save requests to a JSONL file."""
        with open(path, "w", encoding="utf-8") as fh:
            for req in requests:
                json.dump(req, fh)
                fh.write("\n")

    def upload_input_file(self, path: str):
        """Upload a JSONL file using the Files API."""
        if not self.client:
            raise RuntimeError("OpenAI client not available")
        return self.client.files.create(file=open(path, "rb"), purpose="batch")

    def create_batch(self, file_id: str):
        """Submit a batch job for the uploaded file."""
        if not self.client:
            raise RuntimeError("OpenAI client not available")
        return self.client.batches.create(
            input_file_id=file_id,
            endpoint="/v1/chat/completions",
            completion_window="24h",
        )

