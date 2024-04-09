from src.modules.config import Config
import pandas as pd
from pathlib import Path

class DataHandler:
  script_dir = Path(__file__).resolve().parent

  @classmethod
  def getFile(self, filePath):

    if str(filePath).endswith('.csv'):
      file = pd.read_csv(filePath)
      # extend the types (.md / .pdf etc) where necessary

    print(f'[Data Handler]\t- file "{filePath}" loaded successfully.')
    return file
    