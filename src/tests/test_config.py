import unittest
from pathlib import Path
from unittest.mock import patch, mock_open
from src.modules.config import Config

class TestConfig(unittest.TestCase):

    def test_checkScriptDir(self):
        """Test that script_dir is set correctly"""
        expected_dir = Path(__file__).resolve().parent.parent
        self.assertEqual(Config.script_dir.parent, expected_dir)

    def test_check_ConfigStructure(self):
        """Test that the _config dictionary has the expected structure"""
        expected_keys = ['title', 'query', 'app', 'start_time', 'model', 'data', 'server', 'db']
        self.assertEqual(list(Config._config.keys()), expected_keys)

        expected_model_keys = ['transformer', 'name', 'dim', 'device', 'scoreThreshold'] 
        self.assertEqual(list(Config._config['model'].keys()), expected_model_keys)

        expected_data_keys = ['document', 'structure', 'files', 'documents', 'docs', 'metadata', 'ids', 'embeddings']
        self.assertEqual(list(Config._config['data'].keys()), expected_data_keys)

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    def test_loadConfigurationFile(self, mock_file):
        """Test loading the configuration file"""
        config = Config.loadCfg()
        mock_file.assert_called_with(str(Config.script_dir.parent) + '/cfg.json')
        self.assertEqual(config, {"key": "value"})

    @patch.object(Config, 'loadCfg', return_value={"key": "value"})
    def test_init_loads_config_and_returns_merged_dict(self, mock_loadCfg):
        """
        Test that init loads the user config, sets the app and userCfg attributes,
        and returns a dictionary merged from _config and userCfg.
        """
        mock_merge_dicts = unittest.mock.MagicMock(return_value={**Config._config, **{"key": "value"}})
        mock_app = unittest.mock.MagicMock()
        mock_app.utils.merge_dicts = mock_merge_dicts
        
        result = Config.init(modules=mock_app)
        
        self.assertEqual(Config.app, mock_app)
        self.assertEqual(Config.userCfg, {"key": "value"})
        self.assertEqual(result, {**Config._config, **{"key": "value"}})

if __name__ == '__main__':
    unittest.main()
