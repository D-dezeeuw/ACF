from src.modules.config import Config
from sentence_transformers import SentenceTransformer
import chromadb

class Database:
  @classmethod
  def setChromaDB(self):
    db = Config.cfg['db']
    db['connection'] = chromadb.Client()

    print('[Vector DB]\t- ChromaDB initialized successfully.')
    return db['connection']

  @classmethod
  def addDataCollection(self, connection, embeddings, metadatas, ids):
    config = Config.cfg
    db = config['db']

    if len(config['data']['ids']) > 0:
      db['collection'] = connection.create_collection(name=config['db']['group'])
      db['collection'].add(
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
      )

      print(f"[Vector DB]\t- Added collection {config['db']['group']} successfully.")
    else:
      print('[Vector DB]\t- Could not find data to process.')
      return

    return db['collection']