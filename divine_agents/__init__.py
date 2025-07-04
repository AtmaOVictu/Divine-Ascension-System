import logging

logger = logging.getLogger("divine_agents")
if not logger.handlers:
    handler = logging.FileHandler("agents.log")
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
