import json
from typing import Iterable, List, Dict


def build_requests(messages: Iterable[List[Dict[str, str]]]) -> Iterable[str]:
    """Yield JSONL strings for Batch API from a list of chat messages."""
    for idx, msg in enumerate(messages, 1):
        yield json.dumps({
            "custom_id": f"request-{idx}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "gpt-4",
                "messages": msg,
                "max_tokens": 150
            }
        })


def save_jsonl(lines: Iterable[str], path: str) -> None:
    """Save JSONL lines to a file."""
    with open(path, "w", encoding="utf-8") as fh:
        for line in lines:
            fh.write(line + "\n")
