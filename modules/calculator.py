class Calculator:
  __a = 0
  __b = 0
  __operator = ''

  availableoperators = list(["+", "-", "/", "*"])

  def __init__(self, operator, a = 0, b = 0):
    self.__operator = operator
    self.__a = a
    self.__b = b

  def __getraw(self):
    return f"{self.__a}{self.__operator}{self.__b}"

  def __calculate(self, raw):
    return str(eval(raw)) 

  def validateoperator(self):
    for item in list(self.availableoperators):
      if item == self.__operator:
        return True

    return False

  def exec(self):
    if(not self.validateoperator()): 
      raise ValueError(f"Operator ( {self.__operator} ) is not valid.")

    raw = self.__getraw()

    return self.__calculate(raw)