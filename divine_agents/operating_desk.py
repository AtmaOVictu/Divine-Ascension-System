"""Streamlit interface for interacting with agents."""
from __future__ import annotations

from typing import List

import streamlit as st

from .agent import Agent


class Codex:
    def __init__(self, count: int = 3) -> None:
        self.agents: List[Agent] = [Agent(f"Agent{i+1}") for i in range(count)]

    def state_overview(self) -> dict[str, str]:
        return {agent.name: agent.state for agent in self.agents}


def operating_desk(codex: Codex) -> None:
    """Launch the Streamlit operating desk."""
    st.title("Operacijska miza Agentnega sistema")

    st.subheader("Pregled stanja agentov")
    st.write(codex.state_overview())

    st.subheader("Dodajanje novih nalog agentom")
    selected = st.selectbox("Izberite agenta", list(codex.state_overview().keys()))
    task = st.text_input("Vnesite nalogo za agenta")
    if st.button("Dodeli nalogo"):
        st.success(f"Naloga '{task}' je bila dodeljena agentu {selected}.")

    st.subheader("Vizualizacija napredka")
    for agent in codex.agents:
        st.write(f"{agent.name}: {agent.state}")

    st.subheader("Povezovanje agentov za interakcijo")
    a1 = st.selectbox("Izberite prvega agenta", list(codex.state_overview().keys()))
    a2 = st.selectbox("Izberite drugega agenta", list(codex.state_overview().keys()))
    if st.button("Poveži agente"):
        st.success(f"Agent {a1} komunicira z agentom {a2}.")
