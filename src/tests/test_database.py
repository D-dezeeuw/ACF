import unittest
from unittest.mock import patch, MagicMock
from src.modules.config import Config
from sentence_transformers import SentenceTransformer
from src.modules.database import Database
import chromadb

class TestDatabase(unittest.TestCase):
    @patch('chromadb.Client')
    def test_setChromaDB(self, mock_client):
        # Arrange
        Config.cfg = {'db': {}}
        mock_client.return_value = MagicMock()

        # Act
        result = Database.setChromaDB()

        # Assert
        self.assertEqual(result, mock_client.return_value)
        self.assertIn('connection', Config.cfg['db'])
        mock_client.assert_called_once()

    @patch('chromadb.Client')
    def test_addDataCollection_with_data(self, mock_client):
        # Arrange
        Config.cfg = {
            'db': {'group': 'test_group'},
            'data': {'ids': [1, 2, 3]}
        }
        mock_connection = MagicMock()
        mock_collection = MagicMock()
        mock_connection.create_collection.return_value = mock_collection
        embeddings = [MagicMock(), MagicMock(), MagicMock()]
        metadatas = [{'id': 1}, {'id': 2}, {'id': 3}]
        ids = [1, 2, 3]

        # Act
        result = Database.addDataCollection(mock_connection, embeddings, metadatas, ids)

        # Assert
        self.assertEqual(result, mock_collection)
        mock_connection.create_collection.assert_called_once_with(name='test_group')
        mock_collection.add.assert_called_once_with(embeddings=embeddings, metadatas=metadatas, ids=ids)
        self.assertIn('collection', Config.cfg['db'])

    @patch('chromadb.Client')
    def test_addDataCollection_without_data(self, mock_client):
        # Arrange
        Config.cfg = {
            'db': {'group': 'test_group'},
            'data': {'ids': []}
        }
        mock_connection = MagicMock()

        # Act
        result = Database.addDataCollection(mock_connection, [], [], [])

        # Assert
        self.assertIsNone(result)
        mock_connection.create_collection.assert_not_called()

if __name__ == '__main__':
    unittest.main()
