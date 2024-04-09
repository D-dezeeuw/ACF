from src.modules.config import Config

class Output:
  @classmethod
  def message(self, results):
    if results:
      print('[Output]\t- data for output successful.')
      print("\n\nResults:")
      for result in results:
        print(f"{result["title"]} ({result["score"]})")

        body = result.get('body')
        if body:
          print(body + "\n---\n")
      
      print('\n--- end ---\n\n')
    else:
      print('No results provided to output.')