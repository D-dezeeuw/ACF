from src.modules.config import Config

# Runs the script, executed from main.py
class Run():
  
  def init(self, state="server"):
    # 0. Consts
    config = Config.cfg
    app = Config.app
    data = config['data']
    model = config['model']
    db = config['db']
    
    ## INIT ##
    # 1. Start server
    server = Config.app.server() 
    # 2. set the embeddings model
    
    model['transformer'] = app.embed.setModel(model["name"])
    # 3. Initialize the connection
    dbConnection = app.database.setChromaDB()

    ## Write Data ##
    # 4. Import the data
    data['files'] = app.dataHandler.getFile(data["document"])

    # 5. Import the data and embed the data into a vectorgb 
    dbData = app.embed.document(data['files'])
    # 6. Save the data into a vector database
    collection = app.database.addDataCollection(dbConnection, dbData['embeddings'], dbData['metadata'], dbData['ids'])
    
    if state == "setQuery":
      ## Query Data ##
      # 7. Set query and filter data through vector database
      results = app.query.setQuery(collection, config['query'])
      # 8. Output the results in a readable way
      app.output.message(results)

    
    timePassed = app.utils.timePassed()
    print(f'[Run]\t\t- Modules ran successfully. ({timePassed}ms.)')
    return server