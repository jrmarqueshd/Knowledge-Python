import numpy as np

class TextFormatters:
  '''Deal with formatting text
  '''

  def textsplitter(text: str, reference:str=";"):
    '''Split the text

      Args:
        text (str): Text to be 'splitted'
        reference (str, optional): Char used as reference to separator. Defaults to `;`

      Returns:
        list: List of data
    '''

    textsplitted = np.array(text.split(reference))
    textsplitted = map(lambda x: x.strip(), textsplitted)
    
    return list(textsplitted)