def print_diamond(param):
  distance = ord(param.upper()) - ord('A')
  s = ""
  row = 0
  print(distance)
  for d in range(distance):
    spaces = distance - d
    letter = chr(ord('A') + row)
    if row == 0:
      s += "{}{}\n".format(letter, " " * spaces, letter)
    else:
      s += "{}{}{}\n".format(letter, " " * spaces, letter)
    row += 1
  
  for d in range(distance):
    spaces = distance - d
    s += "{}{}\n".format(" " * spaces, chr(ord('A') + row))
  
  print(s)
  return 'A'
