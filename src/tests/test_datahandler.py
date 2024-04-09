import unittest
from unittest.mock import patch
from pathlib import Path
import pandas as pd
from src.modules.dataHandler import DataHandler

class TestDataHandler(unittest.TestCase):
    def setUp(self):
        self.test_csv_file = str(Path(__file__).resolve().parent / 'test_data' / 'test_file.csv')
        self.test_csv_content = "col1,col2\nval1,val2\nval3,val4\n"
        
    def tearDown(self):
        # Clean up any created files if needed
        pass

    @patch('src.modules.dataHandler.pd.read_csv')
    def test_getFile_csv(self, mock_read_csv):
        # Arrange
        mock_read_csv.return_value = pd.DataFrame({'col1': ['val1', 'val3'], 'col2': ['val2', 'val4']})
        
        # Act
        result = DataHandler.getFile(self.test_csv_file)

        # Assert
        mock_read_csv.assert_called_once_with(self.test_csv_file)
        pd.testing.assert_frame_equal(result, pd.DataFrame({'col1': ['val1', 'val3'], 'col2': ['val2', 'val4']}))

    @patch('builtins.print')
    def test_getFile_print(self, mock_print):
        # Arrange
        with patch('src.modules.dataHandler.pd.read_csv') as mock_read_csv:
            mock_read_csv.return_value = pd.DataFrame()
        
            # Act
            DataHandler.getFile(self.test_csv_file)

        # Assert
        mock_print.assert_called_once_with(f'[Data Handler]\t- file "{self.test_csv_file}" loaded successfully.')

if __name__ == '__main__':
    unittest.main()
