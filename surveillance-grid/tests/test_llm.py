import unittest
from src.llm.trainer import Trainer
from src.llm.model import Model
from src.llm.embeddings import Embeddings

class TestLLM(unittest.TestCase):

    def setUp(self):
        self.trainer = Trainer()
        self.model = Model()
        self.embeddings = Embeddings()

    def test_model_initialization(self):
        self.assertIsNotNone(self.model)

    def test_embeddings_creation(self):
        sample_data = ["sample text"]
        embeddings_result = self.embeddings.create_embeddings(sample_data)
        self.assertIsNotNone(embeddings_result)
        self.assertEqual(len(embeddings_result), len(sample_data))

    def test_training_process(self):
        training_data = ["sample text for training"]
        result = self.trainer.train(training_data)
        self.assertTrue(result)

    def tearDown(self):
        del self.trainer
        del self.model
        del self.embeddings

if __name__ == '__main__':
    unittest.main()