from src.modules.config import Config
from sentence_transformers import SentenceTransformer

class Embed:
  @classmethod
  def document(self, documentsData):
    embedded_docs = []
    metadata_docs = []
    ids_docs = []
    config = Config.cfg
    data = config['data']
    structure = None
    if data:
      structure = data["structure"]

    data['embeddings'] = embedded_docs
    data['metadata'] = metadata_docs
    data['ids'] = ids_docs

    # Check if there is data to work with
    if len(data) <=0 or structure == None:
      print('[Embedding]\t- No file to embed, aborting.')
      return
    
    # Combine Question and Answer for each row to prepare your documents in seperate docs
    documents = documentsData.apply(lambda x: x[structure["key"]] + " | " + x[structure["val"]], axis=1)
    
    if hasattr(documents, 'tolist'):
      documents = documents.tolist()
    else:
      print('[Embedding]\t- Dataframe object is not correct.')
      


    # loop through chunks and embed each chunk
    # Gather all the data, embed it and store into a format for chromaDB
    for index, doc in enumerate(documents):
      idLabel = "id" + str(index + 1)
      docSplit = doc.split(" | ")

      ids_docs.append(idLabel)
      embedded_docs.append(config['model']['transformer'].encode(doc).tolist())
      metadata_docs.append({
        "source": idLabel,
        "title": docSplit[0],
        "body": docSplit[1]
      })

    print('[Embeddings]\t- Data embedded successfully.')
    return data

  # Set model for the embeddings
  @classmethod
  def setModel(self, modelName):
    model = SentenceTransformer(modelName, device='cpu')

    timePassed = Config.app.utils.timePassed()
    print(f'[Embeddings]\t- Model "{modelName}" set successfully. ({timePassed}ms.)')
    return model
    
  # Embeds a string and returns it as a vector list
  @classmethod
  def prompt(self, prompt):
    print('MODEL', Config.cfg['model'])
    embed = Config.cfg['model']['transformer'].encode(prompt, normalize_embeddings=False).tolist()
    print(f'[Embeddings]\t- Data string "{prompt}" embedded successfully.')
    return embed