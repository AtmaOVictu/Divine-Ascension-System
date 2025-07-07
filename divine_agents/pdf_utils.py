import re
from typing import List


def extract_text_from_pdf(path: str) -> str:
    """Naively extract visible text from a PDF by regex.

    This avoids external dependencies by scanning for text sequences
    enclosed in parentheses within the PDF's content streams.
    It works for simple PDFs and is sufficient for unit tests.
    """
    try:
        with open(path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        return ""

    streams = re.findall(rb'stream\n(.*?)\nendstream', data, re.S)
    texts: List[str] = []
    for s in streams:
        if b'FlateDecode' in data:
            try:
                import zlib
                s = zlib.decompress(s)
            except Exception:
                pass
        texts.append(s.decode('latin1', errors='ignore'))

    if not texts:
        matches = re.findall(rb'\(([^\)]+)\)', data)
        texts = [m.decode('latin1', errors='ignore') for m in matches]

    return " ".join(texts)
