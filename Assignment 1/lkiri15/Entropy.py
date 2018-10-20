import sys
import math

def parse(fromF, toF):
  file = open(fromF, 'rb')
  out = open(toF, 'w')
  count = [0 for x in range(34)]
  countCouples = [0 for x in range(34 * 34)]
  probs = [0 for x in range(34)]
  probsCouples = [0 for x in range(34 * 34)]
  last = None
  sum = 0
  while 1:
    byte = file.read(1)
    index = 0
    if byte == b'':
      break
    if byte[0] == 32:
      count[0] += 1
      index = 0
    else:
      file.read(1)
      byte = file.read(1)
      index = 1 + byte[0] - 144
      count[index] += 1
    if last != None:
      countCouples[last * 34 + index] += 1
    last = index
    sum += 1
  for i in range(34):
   probs[i] = round(count[i] / sum,7)
  for i in range(34 * 34):
   probsCouples[i] = round(countCouples[i] / (sum - 1), 7)

  entropy = 0
  for i in range(34):
    if probs[i] != 0:
      entropy += probs[i] * math.log(probs[i], 2) * (-1)
  entropyCouples = 0
  for i in range(34 * 34):
    if probsCouples[i] != 0:
      entropyCouples += probsCouples[i] * math.log(probsCouples[i], 2) * (-1)
  out.write(str(entropy) + '\n')
  out.write(str(entropyCouples) + '\n')
  out.write(str(entropyCouples - entropy))


parse(sys.argv[1], sys.argv[2])