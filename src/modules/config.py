from typing import Callable
from pathlib import Path
import json

class Config:
  cfg = {}
  userCfg = {}
  app = {}
  script_dir = Path(__file__).resolve().parent

  _config = {
      'title': str,
      'query': str,
      'app': Callable,
      'start_time': int,
      'model': {
        'transformer': dict,
        'name': str,
        'dim': int,
        'device': str,
        'scoreThreshold': float,
      },
      'data': {
        'document': str,
        'structure': {
          'key':str,
          'val':str
        },
        'files': tuple,
        'documents': tuple,
        'docs': tuple,
        'metadata': tuple,
        'ids': tuple,
        'embeddings': dict
      },
      'server': {
        'api': Callable
      },
      'db': {
        'connection': dict,
        'collection': Callable,
        'group': str,
        'prefix': str
      }
    }

  @classmethod
  def loadCfg(self):
    cfgData = None
    userConfig = None
    file = open(str(self.script_dir.parent) + '/cfg.json')
    if file:
      cfgData = file.read();
      return json.loads(cfgData)
    else:
      return {}

  @classmethod
  def init(self, modules = None):
    if modules != None:
      self.app = modules
      self.userCfg = self.loadCfg()
      self.cfg = self.app.utils.merge_dicts(self._config, self.userCfg)

    print(f'\n[Config]\t- User configuration loaded successfully.')
    return self.cfg