from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class EmbeddingsManager:
    def __init__(self, embedding_dim):
        self.embedding_dim = embedding_dim
        self.embeddings = {}

    def add_embedding(self, key, vector):
        if len(vector) != self.embedding_dim:
            raise ValueError(f"Vector must be of dimension {self.embedding_dim}")
        self.embeddings[key] = vector

    def get_embedding(self, key):
        return self.embeddings.get(key)

    def compute_similarity(self, key1, key2):
        if key1 not in self.embeddings or key2 not in self.embeddings:
            raise ValueError("Both keys must exist in the embeddings")
        return cosine_similarity([self.embeddings[key1]], [self.embeddings[key2]])[0][0]

    def get_all_embeddings(self):
        return self.embeddings

    def clear_embeddings(self):
        self.embeddings.clear()