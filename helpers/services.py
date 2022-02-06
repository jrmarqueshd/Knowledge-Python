import csv

class CSVHelpers:
  '''Deal with CSVs

    Args:
      dirfile (str): File location
  '''

  __dirfile = None

  def __init__(self, dirfile):
    self.__dirfile = dirfile

  def getdata(self):
    '''Get CSV data

      Raises:
        Exception: File not found.

      Returns:
        list: Data extracted from csv
    '''

    data = list()

    try:
      with open(self.__dirfile) as csvfile:
        csvreader = csv.reader(csvfile)

        for line in csvreader:
          data.append(line[0])  
    except IOError:
      raise Exception("The specified file was not found.")
    finally:
      csvfile.close()

    return data

class JSONHelpers:
  '''Deal with JSONs

    Args:
      dirfile (str): File directory and name. Not need extension
  '''

  __dirfile = ""
  __data = ""

  def __init__(self, dirfile:str):
    self.__dirfile = dirfile
  
  def __extensionremover(dirfile: str):
    '''Removes extension from filename

      Args:
        dirfile (str): Filename to be extension removed

      Returns:
        str: Filename without extension
    '''

    if dirfile.find(".") == -1:
      return dirfile

    return dirfile[0:dirfile.rfind(".")]

  def save(self, data: str):
    '''Save data in .json file

      data (str): Data to be written on the file.
    '''

    with open(f'{JSONHelpers.__extensionremover(self.__dirfile)}.json', 'w') as jsonfile:
      jsonfile.write(data)
      jsonfile.close()
