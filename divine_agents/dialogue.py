from typing import List, Optional
from .agent import Agent
from .pdf_utils import extract_text_from_pdf


def philosophical_dialogue(agent1: Agent, agent2: Agent, pdf_path: Optional[str] = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    If ``pdf_path`` is provided, the dialogue begins with text extracted
    from the PDF to demonstrate integration with document inputs.
    """
    lines: List[str] = []

    if pdf_path:
        pdf_text = extract_text_from_pdf(pdf_path)
        if pdf_text:
            lines.append(f"Iz izvlečka PDF: {pdf_text}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
