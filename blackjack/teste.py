def printtexto(string):
  if not isinstance(string,str):
    raise ValueError(f'expect a string type, got:{type(string)}')
  print(string)