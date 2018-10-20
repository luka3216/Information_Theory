import sys

def parse(fromF, toF):
  file = open(fromF, 'rb')
  out = open(toF, 'w')
  count = [0 for x in range(34)]
  countCouples = [0 for x in range(34 * 34)]
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
  for i in range(33):
   out.write(str("{:9.7f}".format(round(count[i] / sum,7))) + ' ')
  out.write(str("{:9.7f}".format(round(count[33] / sum, 7))) + '\n')
  for i in range(34 * 34 - 1):
   out.write(str("{:9.7f}".format(round(countCouples[i] / (sum - 1),7))) + ' ')
  out.write(str("{:9.7f}".format(round(countCouples[34 * 34 - 1] / (sum - 1), 7))) + '\n')

parse(sys.argv[1], sys.argv[2])