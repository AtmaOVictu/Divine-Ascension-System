from typing import List
from .agent import Agent


def multi_agent_debate(agents: List[Agent], rounds: int = 1) -> List[str]:
    """Run a multi-round debate between agents with emotional shifts."""
    transcript: List[str] = []
    for _ in range(rounds):
        for ag in agents:
            transcript.append(f"{ag.name} ({ag.state}): {ag.respond('Kaj je resnica?')}")
        for ag in agents:
            emotion_value = min(ag.emotion + 0.3, 1.0)
            emotion_type = 'anger' if ag.state == 'Ego' else 'joy'
            ag.update_emotion(emotion_value, emotion_type)
            transcript.append(f"{ag.name} prehaja v stanje: {ag.transition()}")
    return transcript

