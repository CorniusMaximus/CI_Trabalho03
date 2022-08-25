import re
Proposicao = re.compile(r'[A-Za-z0-9]+')

#Proposicao = [A-Za-z0-9]+
#Constante = T|F
#AbreParen = (
#FechaParen = )
#OperatorUnario = ¬
#OperatorBinario = ∨|∧|→|↔
#Formula = Constante|Proposicao|FormulaUnaria|FormulaBinaria
#FormulaUnaria = (AbreParen)(OperatorUnario)(Formula)(FechaParen)
#FormulaBinaria = (AbreParen)(OperatorBinario)(Formula)(Formula)(FechaParen)

def Read(file): 
  with open(file) as f:
    line = f.readline()
    line = line. rstrip('\n')
    countDown = int(line)

    for i in range(countDown): 
      pertence = True
      line = f.readline()  
      if not line or countDown == 0:
        break        
      res = line.split()  
      pertence = Formula(res)
        
      if pertence == True:
        print("válida")
      else:
        print("inválida")



def Formula(formula):
  contParen = 0
  cont = 0
  
  if formula[0] == 'T' or formula[0] == 'F':
    return True
    
  elif Proposicao.fullmatch(formula[0]) is not None:
    if len(formula) > 1:
      return False
    
    return True
    
  elif formula[0] == '(':
    for i in formula: 
      cont += 1
      
      if i == '(':
        contParen += 1
      elif i == ')':
        contParen -= 1
        if contParen == 0 and cont < len(formula):
          return False
    
    if formula[-1] != ')':
      return False
      
    if formula[1] == '¬':      
      return FormulaUnaria(formula)
      
    elif formula[1] == '∨' or formula[1] == '∧' or formula[1] == '→' or formula[1] == '↔':
      return FormulaBinaria(formula)
    else:
      return False
  else:
    return False


def FormulaUnaria(forUn):
  del forUn[0]
  del forUn[0]
  del forUn[-1]

  if forUn[0] == '(' and forUn[-1] != ')':
    return False
    
  return Formula(forUn)

def FormulaBinaria(forBin):
  del forBin[0]
  del forBin[0]
  del forBin[-1]

  formula01 = []

  openParen = False
  contParen = 0
  
  for01 = True
  for02 = True

  if forBin[0] == '(':
    openParen = True
    
    for i in forBin:
      formula01.append(i)
      if i == '(':
        contParen += 1
      elif i == ')':
        contParen -= 1
        if contParen == 0:
          openParen = False
          break

    if(openParen):
      return False

    del forBin[0 : len(formula01)]

    for01 = Formula(formula01)
    for02 = Formula(forBin)

    return for01 and for02
  else:
    formula01.append(forBin[0])
    
    del forBin[0]
    
    for01 = Formula(formula01)
    for02 = Formula(forBin)
    
    return for01 and for02