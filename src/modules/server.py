from src.modules.config import Config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

class filter_query(BaseModel):
    query: str

def setMiddleware(api):
  api.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
  )

def setRouting(api):
  config = Config.cfg
  app = Config.app
  db = config.get('db') or None
  

  @api.get("/")
  async def root():
    return {"message": "ACF is healthy"}

  @api.post("/filter")
  async def filter(response: filter_query):
    query = str(response.query)
    if Config.cfg and 'db' in Config.cfg and 'collection' in Config.cfg['db']:
        collection = Config.cfg['db']['collection']
        results = app.query.setQuery(collection, query)
        app.output.message(results)
        return {"results": results}
    else:
        return {"error": "Database configuration not found"}
def Server():
  api = FastAPI()

  setMiddleware(api)
  setRouting(api)

  timePassed = Config.app.utils.timePassed()
  print(f'[Api]\t\t- Initialized successfully. ({timePassed}ms.)')
  return api