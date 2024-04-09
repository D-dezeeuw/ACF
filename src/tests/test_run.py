import unittest
from unittest.mock import MagicMock, patch
from src.modules.config import Config
from src.modules.run import Run

class TestRun(unittest.TestCase):
    @patch('src.modules.config.Config.app')
    @patch('src.modules.config.Config.cfg')
    def test_run_init_server(self, mock_cfg, mock_app):
        # Mock the necessary objects and methods
        mock_server = MagicMock()
        mock_dbConnection = MagicMock()
        mock_collection = MagicMock()

        mock_app.server.return_value = mock_server
        mock_app.embed.setModel.return_value = 'mock_transformer'
        mock_app.database.setChromaDB.return_value = mock_dbConnection
        mock_app.dataHandler.getFile.return_value = 'mock_files'
        mock_app.embed.document.return_value = {
            'embeddings': 'mock_embeddings',
            'metadata': 'mock_metadata',
            'ids': 'mock_ids'
        }
        mock_app.database.addDataCollection.return_value = mock_collection

        # Set up the mock configuration
        mock_cfg.update({
            'data': {'document': 'mock_document'},
            'model': {'name': 'mock_model'},
            'db': {}
        })

        # Create an instance of the Run class
        run = Run()

        # Call the init method with state "server"
        result = run.init(state="server")

        # Assert the expected function calls and results
        mock_app.server.assert_called_once()
        mock_app.embed.setModel.assert_called_once('mock_model')
        mock_app.database.setChromaDB.assert_called_once()
        mock_app.dataHandler.getFile.assert_called_once_with('mock_document')
        mock_app.embed.document.assert_called_once_with('mock_files')
        mock_app.database.addDataCollection.assert_called_once_with(
            mock_dbConnection, 'mock_embeddings', 'mock_metadata', 'mock_ids'
        )
        mock_app.query.setQuery.assert_not_called()
        mock_app.output.message.assert_not_called()

        self.assertEqual(result, mock_server)

    @patch('src.modules.config.Config.app')
    @patch('src.modules.config.Config.cfg', new_callable=MagicMock)
    def test_run_init_server(self, mock_cfg, mock_app):
        # Mock the necessary objects and methods
        mock_server = MagicMock()
        mock_dbConnection = MagicMock()
        mock_collection = MagicMock()

        mock_app.server.return_value = mock_server
        mock_app.embed.setModel.return_value = 'mock_transformer'
        mock_app.database.setChromaDB.return_value = mock_dbConnection
        mock_app.dataHandler.getFile.return_value = 'mock_files'
        mock_app.embed.document.return_value = {
            'embeddings': 'mock_embeddings',
            'metadata': 'mock_metadata',
            'ids': 'mock_ids'
        }
        mock_app.database.addDataCollection.return_value = mock_collection

        # Set up the mock configuration
        mock_cfg.__getitem__.return_value = {
            'document': 'mock_document',
            'name': 'mock_model'
        }

        # Create an instance of the Run class
        run = Run()

        # Call the init method with state "server"
        result = run.init(state="server")

        # Assert the expected function calls and results
        mock_app.server.assert_called_once()
        mock_app.embed.setModel.assert_called_once_with('mock_model')
        mock_app.database.setChromaDB.assert_called_once()
        mock_app.dataHandler.getFile.assert_called_once_with('mock_document')
        mock_app.embed.document.assert_called_once_with('mock_files')
        mock_app.database.addDataCollection.assert_called_once_with(
            mock_dbConnection, 'mock_embeddings', 'mock_metadata', 'mock_ids'
        )
        mock_app.query.setQuery.assert_not_called()
        mock_app.output.message.assert_not_called()

        self.assertEqual(result, mock_server)


if __name__ == '__main__':
    unittest.main()
