import math
import json
from formulas import formulas_

#TODO: MAKE NORMAL TO GET SQUARE SIGN AND π
def get_arca_value(equation, type_, num):
  with open('table_of_values_arc.json', 'r') as file:
    data = json.load(file)
    #print(data['acos'])
    #print(b'%s', num)
    return data[type_][num]

def get_arca(equation: str):
  num = equation.split('=')[1]
  things = ['sin', 'cos', 'tg', 'ctg']

  # return int('0.5')
  for i in things:
    if i in equation:
      if i == 'sin':
        #'asin ' + num + ' equals: ' +
        return get_arca_value(equation=equation, type_='asin', num=num), 'a' + i
      elif i == 'cos':
        return get_arca_value(equation=equation, type_='acos', num=num), 'a' + i
      elif i == 'tg':
        return get_arca_value(equation=equation, type_='atg', num=num), 'a' + i
      else:
        return get_arca_value(equation=equation, type_='actg', num=num), 'a' + i

  else:
    return 'fuck you'


def solve_this(equation: str):


  if '√' in equation:
    equation = equation.replace('√', 'square_of') 

  arca = get_arca(equation=equation)
  #print(arca)
  return formulas_(*arca)
  

#√
try:
  print(solve_this('cosx=-(1/2)'))
except KeyError as e:
  print(e, '\nInvalid value, pls check validity of equation')
