"""Initialization for the divine_agents package."""

from __future__ import annotations

import json
import logging
import os

from .agent import Agent

DEFAULT_STATE = "Ego"
DEFAULT_TENSION = 0.0
DEFAULT_EMOTION = 0.0

_config = {}
global_agent: Agent | None = None


def initialize_system() -> None:
    """Set up logging and load optional configuration."""
    global global_agent, _config

    logging.basicConfig(level=logging.INFO)
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as fh:
            _config = json.load(fh)
        logging.info("Configuration loaded from %s", config_path)
    else:
        _config = {}
        logging.info("No configuration file found at %s", config_path)

    global_agent = Agent(
        _config.get("name", "GlobalAgent"),
        state=_config.get("state", DEFAULT_STATE),
        tension=_config.get("tension", DEFAULT_TENSION),
        emotion=_config.get("emotion", DEFAULT_EMOTION),
    )


def get_global_agent() -> Agent:
    """Return the singleton global agent."""

    return global_agent


# Initialize system on import
initialize_system()

__all__ = [
    "Agent",
    "initialize_system",
    "get_global_agent",
    "global_agent",
    "DEFAULT_STATE",
    "DEFAULT_TENSION",
    "DEFAULT_EMOTION",
]

