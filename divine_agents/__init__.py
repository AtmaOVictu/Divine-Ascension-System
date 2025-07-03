"""Paket `divine_agents` omogoča simulacijo ontoloških agentov.

Modul združuje razrede in funkcije za upravljanje filozofskih stanj ter
izvajanje dialogov med agenti. Namenjen je modeliranju prehodov med stanjema
Ego, Jaz in Enotnost na podlagi čustev in napetosti.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
