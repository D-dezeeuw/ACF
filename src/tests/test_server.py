from unittest import TestCase
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
import src.main
from src.modules.server import Server
from src.modules.querying import Query

class TestServer(TestCase):
    def setUp(self):
        self.api = Server()
        self.client = TestClient(self.api)

    @patch('src.modules.config.Config')
    def test_root_endpoint(self, mock_config):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "ACF is healthy"})

    @patch('src.modules.config.Config')
    @patch('src.modules.querying.Query.setQuery')
    @patch('src.modules.config.Config.app.output.message')
    def test_filter_endpoint(self, mock_message, mock_set_query, mock_config):
      mock_config.cfg = {'db': {'collection': 'mock_collection'}}
      # Set up the mock configuration without the 'db' key
      mock_config.app = {'query': MagicMock()}

      query = "test query"
      response = self.client.post("/filter", json={"query": query})

      self.assertEqual(response.status_code, 200)
      mock_set_query.assert_not_called()
      mock_message.assert_not_called()

    @patch('src.modules.config.Config')
    @patch('src.modules.querying.Query.setQuery')
    @patch('src.modules.config.Config.app.output.message')
    def test_filter_endpoint_missing_db_config(self, mock_message, mock_set_query, mock_config):
        # Set up the mock configuration without the 'db' key
        mock_config.cfg = {}
        mock_config.app = {'query': MagicMock()}

        query = "test query"
        response = self.client.post("/filter", json={"query": query})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'error': 'Database configuration not found'})

        mock_set_query.assert_not_called()
        mock_message.assert_not_called()
       


if __name__ == '__main__':
    unittest.main()