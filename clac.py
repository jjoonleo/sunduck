inputString = input().strip()
data = []

if inputString[0].isdigit():
  data.append(['+', 0])
  for i in inputString:
    if not i.isdigit():
      break
    data[-1][1] = data[-1][1] * 10 + int(i)

