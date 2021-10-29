

def formulas_(arca_value, type_):

  if 'ПЂ' in arca_value:
    arca_value = arca_value.replace('ПЂ', 'π')
  #±±±±±±±±±±±±±
  formulas__ = {
      'asin': f'x = (-1)^k*{arca_value} + πk, n ∈ Z',
      'acos': f'x = ±{arca_value} + 2πn, n ∈ Z',
      'atg': f'x = {arca_value} + πn, n ∈ Z',
      'actg': f'x = {arca_value} + πn, n ∈ Z'
    }

  #print(formulas__[type_])
  return formulas__[type_].replace('square_of', '√')

#print(formulas4(1, 'q'))

