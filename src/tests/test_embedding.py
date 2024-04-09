import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import src.main
from src.modules.config import Config
from src.modules.embedding import Embed

class TestEmbed(unittest.TestCase):
    def setUp(self):
        # Set up test data
        self.test_data = pd.DataFrame({
            'question': ['What is the capital of France?', 'Who painted the Mona Lisa?'],
            'answer': ['Paris', 'Leonardo da Vinci']
        })
        Config.cfg = {
            'data': {
                'structure': {
                    'key': 'question',
                    'val': 'answer'
                }
            },
            'model': {
                'transformer': MagicMock()
            }
        }

    @patch('builtins.print')
    def test_document_no_data(self, mock_print):
        # Arrange
        Config.cfg['data'] = {}
        
        # Act
        result = Embed.document(self.test_data)

        # Assert
        mock_print.assert_called_once_with('[Embedding]\t- No file to embed, aborting.')
        self.assertIsNone(result)

    def test_document_success(self):
        # Act
        result = Embed.document(self.test_data)

        # Assert
        self.assertEqual(len(result['embeddings']), 2)
        self.assertEqual(len(result['metadata']), 2)
        self.assertEqual(len(result['ids']), 2)
        Config.cfg['model']['transformer'].encode.assert_called()

    @patch('src.modules.embedding.SentenceTransformer')
    def test_setModel(self, mock_transformer):
        # Arrange
        model_name = 'all-MiniLM-L6-v2'
        mock_transformer.return_value = 'mocked_model'

        # Act
        result = Embed.setModel(model_name)

        # Assert
        mock_transformer.assert_called_once_with(model_name, device='cpu')
        self.assertEqual(result, 'mocked_model')

    def test_prompt(self):
        # Arrange
        test_prompt = 'This is a test prompt'
        Config.cfg['model']['transformer'].encode.return_value.tolist.return_value = [0.1, 0.2, 0.3]
        
        # Act
        result = Embed.prompt(test_prompt)

        # Assert
        Config.cfg['model']['transformer'].encode.assert_called_once_with(test_prompt, normalize_embeddings=False)
        self.assertIsInstance(result, list)
  
    def test_document_empty(self):
        # Arrange
        empty_data = pd.DataFrame()
        
        # Act
        result = Embed.document(empty_data)

        # Assert
        self.assertEqual(len(result['embeddings']), 0)
        self.assertEqual(len(result['metadata']), 0)
        self.assertEqual(len(result['ids']), 0)

    def test_prompt_empty(self):
      # Arrange
      empty_prompt = ''
      mock_encoded = MagicMock()
      mock_encoded.tolist.return_value = [0.1, 0.2, 0.3]  # This should be the expected list
      Config.cfg['model']['transformer'].encode.return_value = mock_encoded
      
      # Act
      result = Embed.prompt(empty_prompt)

      # Assert
      Config.cfg['model']['transformer'].encode.assert_called_once_with(empty_prompt, normalize_embeddings=False)
      self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
