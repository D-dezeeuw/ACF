from src.modules.config import Config
from dataclasses import dataclass
import time

@dataclass
class Utils:
  start_time = time.time()
  
  @classmethod
  def merge_dicts(self, dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if isinstance(value, dict):
            merged[key] = self.merge_dicts(merged.get(key, {}), value)
        else:
            merged[key] = value
    return merged

  @classmethod
  def timePassed(self):
    return round(time.time() - self.start_time, 2)