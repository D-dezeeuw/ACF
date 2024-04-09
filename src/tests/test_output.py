import unittest
from unittest.mock import patch
from src.modules.output import Output

class TestOutput(unittest.TestCase):

    @patch('builtins.print')
    def test_message_with_results(self, mock_print):
        # Arrange
        results = [
            {'title': 'Title 1', 'score': 0.9, 'body': 'Body 1'},
            {'title': 'Title 2', 'score': 0.8, 'body': 'Body 2'}
        ]
        
        # Act
        print('THESE ARE RESULTS', results)
        Output.message(results)

        # Assert
        expected_calls = [
            unittest.mock.call('[Output]\t- data for output successful.'),
            unittest.mock.call('\n\nResults:'),
            unittest.mock.call('Title 1 (0.9)'),
            unittest.mock.call('Body 1\n---\n'),
            unittest.mock.call('Title 2 (0.8)'),
            unittest.mock.call('Body 2\n---\n'),
            unittest.mock.call('\n--- end ---\n\n')
        ]
        mock_print.assert_has_calls(expected_calls)

    @patch('builtins.print')
    def test_message_with_no_results(self, mock_print):
        # Arrange
        results = []
        
        # Act
        Output.message(results)

        # Assert
        mock_print.assert_called_once_with('No results provided to output.')

    @patch('builtins.print')  
    def test_message_with_missing_body(self, mock_print):
        # Arrange
        results = [
            {'title': 'Title 1', 'score': 0.9},
            {'title': 'Title 2', 'score': 0.8, 'body': 'Body 2'}
        ]
        
        # Act
        Output.message(results)

        # Assert
        expected_calls = [
            unittest.mock.call('[Output]\t- data for output successful.'),
            unittest.mock.call('\n\nResults:'),
            unittest.mock.call('Title 1 (0.9)'),
            unittest.mock.call('Title 2 (0.8)'),
            unittest.mock.call('Body 2\n---\n'),
            unittest.mock.call('\n--- end ---\n\n')
        ]
        mock_print.assert_has_calls(expected_calls)

if __name__ == '__main__':
    unittest.main()
