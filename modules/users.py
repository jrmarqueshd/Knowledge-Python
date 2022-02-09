# dependecies

import sys 
import json
from slugify import slugify

# modules
sys.path.insert(0, './')
from helpers.services import CSVHelpers as csvhelpers
from helpers.formatters import TextFormatters as textformatters

class Users:
  '''Deal with users
  '''

  __header = list()
  __users = list()
  
  # overloading methods

  def __init__(self):
    data = csvhelpers("./assets/users.csv").getdata() 
    self.__header = Users.__getheader(data)
    self.__users = Users.__getusers(data)

  # private methods

  def __getheader(data: list):
    '''Get the CSV header data, removes him from original data, and 'slugify' each header item.

      Args:
        data (list): All data from CSV

      Returns:
        list: header table formatted
    '''

    headerlist = textformatters.textsplitter(data.pop(0))
    headerslugified = map(lambda headeritem: slugify(headeritem, separator='_'), headerlist)

    return list(headerslugified)

  def __getusers(users: list):
    '''Get the users, and convert the data of each to an list.

      Args:
        users (list): Users collected from CSV

      Returns:
        list: Users from CSV formatted in matrix
    '''

    matrixusers = list()

    for user in users:
      matrixusers.append(textformatters.textsplitter(user))

    return matrixusers
    
  # public methods

  def getusersinfo(self):
    '''Get users infos

      Returns:
        str: Users in JSON beautified
    '''

    userslist = list()

    for user in self.__users:
      userinfo = {}
      
      for headerindex, headeritem in enumerate(self.__header):
        userinfo[headeritem] = user[headerindex]

      userslist.append(userinfo)

    return json.dumps(userslist, sort_keys=True, indent=2)  
