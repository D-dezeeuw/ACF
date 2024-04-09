import unittest
from unittest.mock import MagicMock, patch
from src.modules.querying import Query
from src.modules.config import Config

class TestQuery(unittest.TestCase):

    def setUp(self):
        Config.cfg = {
            'model': {
                'n_results': 5,
                'scoreThreshold': 7.5
            }
        }
        Config.app = MagicMock()
        Config.app.embed.prompt.return_value = [0.1, 0.2, 0.3]

    @patch('builtins.print')
    def test_setQuery_missing_collection(self, mock_print):
        # Arrange
        collection = None
        prompt = "Test prompt"

        # Act
        result = Query.setQuery(collection, prompt)

        # Assert
        mock_print.assert_called_once_with('[Query] - Missing collection or prompt')
        self.assertIsNone(result)

    @patch('builtins.print')
    def test_setQuery_missing_prompt(self, mock_print):
        # Arrange
        collection = MagicMock()
        prompt = None

        # Act
        result = Query.setQuery(collection, prompt)

        # Assert
        mock_print.assert_called_once_with('[Query] - Missing collection or prompt')
        self.assertIsNone(result)

    def test_setQuery_no_results(self):
        # Arrange
        collection = MagicMock()
        collection.query.return_value = {'metadatas': None}
        prompt = "Test prompt"

        # Act
        result = Query.setQuery(collection, prompt)

        # Assert
        self.assertEqual(result, [])

    def test_setQuery_with_results(self):
       # Arrange
        collection = MagicMock()
        collection.query.return_value = {
            'metadatas': [[
                {'title': 'Result 1', 'body': 'Body 1'},
                {'title': 'Result 2', 'body': 'Body 2'}
            ]],
            'distances': [[0.2, 1.5]]  # Updated distances to yield scores above the threshold
        }
        prompt = "Test prompt"

        # Act
        result = Query.setQuery(collection, prompt)

        # Assert
        self.assertEqual(len(result), 1)  # Only one result should meet the threshold
        self.assertEqual(result[0]['title'], 'Result 1')
        self.assertEqual(result[0]['score'], 9.0)  # Updated expected score
        self.assertEqual(result[0]['body'], 'Body 1')

    @patch('builtins.print')
    def test_setQuery_exception(self, mock_print):
        # Arrange
        collection = MagicMock()
        test_exception = Exception('Test exception')
        collection.query.side_effect = test_exception
        prompt = "Test prompt"

        # Act
        result = Query.setQuery(collection, prompt)

        # Assert
        self.assertEqual(result, [])
        mock_print.assert_called_once_with('could not find any results:\n', test_exception)

if __name__ == '__main__':
    unittest.main()
