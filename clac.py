inputString = input().strip()
data = []

if inputString[0].isdigit():
  data.append(['+', 0])
  for i in inputString:
    if not i.isdigit():
      break
    data[-1][1] = data[-1][1] * 10 + int(i)

i = 1

while i < len(inputString):
  if inputString[i] == '+' or inputString[i] == '-':
    data.append([inputString[i], 0])
    i += 1
    while i < len(inputString):
      if not inputString[i].isdigit():
        break
      data[-1][1] = data[-1][1] * 10 + int(inputString[i])
      i += 1
  else:
    i += 1

