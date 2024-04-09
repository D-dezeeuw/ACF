from src.modules.config import Config

class Query():
  results = []

  @classmethod
  def setQuery(self, collection, prompt, n_results="no"):
    
    if n_results == "no":
      n_results = Config.cfg['model']['n_results']

    app = Config.app
    scoreThreshold = Config.cfg['model']['scoreThreshold']
    resultsArray = []

    if not collection or not getattr(collection, 'query') or not prompt:
      print('[Query] - Missing collection or prompt')
      return

    try:
      results = collection.query(
        query_embeddings= app.embed.prompt(prompt),
        n_results=n_results
      )
    except Exception as e:
      print('could not find any results:\n', e)
      return []

    # Try to get the results from the chromadb proximity filter
    try:
      if results['metadatas']:
        data = results['metadatas'][0]

        # Go through the results and filter on the scoreThreshold.
        # Cherrypick and return the data that we need

        for index, result in enumerate(data):
          
          # Normalize the distance from: 0 - 10.00
          distance = round( ((2 - results['distances'][0][index]) /2) * 10, 2)

          # If the distance meets our scoreThreshold requirement, add it to our results.
          if distance > scoreThreshold:
            resultData = {
              "index": (index + 1),
              "title": result['title'],
              "score": distance
            }
            # The first (best)match also gets the answer
            if index == 0:
              resultData["body"] = result['body']

            resultsArray.append(resultData)
    except Exception as e: 
      print('could not find any results:\n', e)
      return []

    print('[Querying]\t- data queried successfully.')
    return resultsArray
      