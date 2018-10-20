import sys
import math

def parse(fromF, toF):
  file = open(fromF, 'rb')
  out = open(toF, 'w')
  length = int(file.readline())
  lengths = [int(x) for x in file.readline().split()]
  sum = 0
  last = 0b0
  lastSize = 0
  result = []
  for len in lengths:
    sum += float(1) / math.pow(2, len)
  if sum <= 1:
    for len in lengths:
      if lastSize == 0:
        result.append(str(last).zfill(len))
        lastSize = len
      else:
        while len < lastSize:
          lastSize = lastSize - 1 
          last = int(last / 2)
        last += 1
        while len > lastSize:
          last *= 2
          lastSize += 1
        result.append(str(bin(last)[2:]).zfill(len))
  for res in result:
    out.write(res + ' ')



parse(sys.argv[1], sys.argv[2])