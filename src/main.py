from dataclasses import dataclass, field
from src.modules.config import Config
from src.modules.run import Run
from src.modules.dataHandler import DataHandler
from src.modules.database import Database
from src.modules.embedding import Embed
from src.modules.querying import Query
from src.modules.output import Output
from src.modules.server import Server
from src.modules.utils import Utils

@dataclass
class App:
  config: Config = Config # Configuration object
  utils: Utils = Utils # Set of generic utilities
  run: Run = Run # Runs the program and executes the various modules
  embed: Embed = Embed # Handles embedding tasks for files and prompts
  dataHandler: DataHandler = DataHandler # Handles data operations like reading files
  database: Database = Database # Sets up the in-memory chromaDB
  query: Query = Query # Sets prompts to query against the vector database
  output: Output = Output # Outputs the results in a readable way
  server: Server = Server # Creates a server to provide an web API

Config.init(App())

if __name__ == "__main__":
  api = Config.app.run.init('setQuery')
  print("[Main]\t\t- ACF App initialized.")
elif __name__ == "main" or  __name__ == "src.main":
  api = Config.app.run.init('server')
  print("[Main]\t\t- WSGI setup initialized.")
  