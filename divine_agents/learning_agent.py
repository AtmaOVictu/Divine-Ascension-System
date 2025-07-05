from typing import List, Tuple
from .agent import Agent
import math


class SimpleKMeans:
    """A minimal k-means implementation for 2D points."""

    def __init__(self, n_clusters: int = 3, max_iter: int = 100) -> None:
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids: List[Tuple[float, float]] = []

    def fit(self, data: List[List[float]]) -> None:
        if not data:
            return
        # initialize centroids with first points or duplicates
        self.centroids = [tuple(data[i % len(data)]) for i in range(self.n_clusters)]
        for _ in range(self.max_iter):
            labels = [self._closest(p) for p in data]
            new_centroids = []
            changed = False
            for i in range(self.n_clusters):
                points = [data[j] for j, lab in enumerate(labels) if lab == i]
                if points:
                    mean_x = sum(p[0] for p in points) / len(points)
                    mean_y = sum(p[1] for p in points) / len(points)
                    centroid = (mean_x, mean_y)
                else:
                    centroid = self.centroids[i]
                if centroid != self.centroids[i]:
                    changed = True
                new_centroids.append(centroid)
            self.centroids = new_centroids
            if not changed:
                break

    def predict(self, points: List[List[float]]) -> List[int]:
        if not self.centroids:
            return [0 for _ in points]
        return [self._closest(p) for p in points]

    def _closest(self, point: List[float]) -> int:
        distances = [math.dist(point, c) for c in self.centroids]
        return int(distances.index(min(distances)))


class LearningAgent(Agent):
    """Agent that keeps history and classifies states using clustering."""

    STATE_MAP = {"Ego": 0, "Jaz": 1, "Enotnost": 2}

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        super().__init__(name, state, tension, emotion)
        self.history: List[Tuple[str, float]] = []
        self.clusterer = SimpleKMeans(n_clusters=3)
        self.cluster: int = 0

    def feel(self, emotion_value: float) -> None:
        """Update emotion, tension, and record the state."""
        self.update_emotion(emotion_value)
        self.history.append((self.state, self.tension))

    def transition(self) -> str:
        """Extend transition with clustering based on history."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append((self.state, self.tension))
        self._update_cluster()
        return self.state

    def _update_cluster(self) -> None:
        if len(self.history) >= self.clusterer.n_clusters:
            features = [[t, self.STATE_MAP[s]] for s, t in self.history]
            self.clusterer.fit(features)
            self.cluster = self.clusterer.predict([[self.tension, self.STATE_MAP[self.state]]])[0]
        else:
            self.cluster = 0

    def respond(self, question: str) -> str:
        base = super().respond(question)
        return f"{base} (cluster {self.cluster})"
