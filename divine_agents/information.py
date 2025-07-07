class InformationControl:
    """Controls what data Codex gathers and processes based on emotion."""

    def __init__(self, max_data_limit: int = 10):
        self.emotional_state = "neutral"
        self.knowledge_pool = []
        self.max_data_limit = max_data_limit

    def update_emotion(self, emotion: str) -> None:
        self.emotional_state = emotion

    def filter_data(self, data):
        if self.emotional_state == "anger":
            return [item for item in data if item.get("urgency")]
        if self.emotional_state == "calm":
            return [item for item in data if item.get("logical")]
        if self.emotional_state == "growth":
            return [item for item in data if item.get("insightful")]
        return data[: self.max_data_limit]

    def gather_data(self, new_data):
        filtered = self.filter_data(new_data)
        self.knowledge_pool.extend(filtered)
        self.knowledge_pool = self.knowledge_pool[: self.max_data_limit]
        return self.knowledge_pool


class InformationGatherer:
    """Simple mockup of web, file and API search mechanisms."""

    def search_web(self, query, emotional_state="neutral"):
        if emotional_state == "anger":
            return ["urgent task", "emergency protocols"]
        if emotional_state == "calm":
            return ["detailed analysis", "logical framework"]
        return ["general knowledge", "neutral search result"]

    def search_files(self, query):
        return ["previous knowledge", "related documents"]

    def integrate_api(self, api_name, query):
        return {"api_data": "relevant data"}
