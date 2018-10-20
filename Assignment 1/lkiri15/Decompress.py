import sys
import math
import struct

def decode(buff):
  return int(buff, 2).to_bytes(len(buff) // 8, byteorder='big')

def parse(fromF, codeF, toF):
  file = open(fromF, 'rb')
  code = open(codeF, 'rb')
  out = open(toF, 'wb')
  lengths = dict(zip([code.readline().strip() for x in range(34)], [int(x) for x in range(34)]))
  max = 0
  for i in lengths:
    if len(i) > max:
      max = len(i)
  buff = b''
  last = -1
  while 1:
    byte = file.read(1)
    if byte == b'':
      break
    buff += bytearray("{0:08b}".format(byte[0]).encode("ascii"))
  for i in range(len(buff) - 1, 0, -1):
    if buff[i] == b'1'[0]:
      buff = buff[:i]
      break
  
  last = -1
  buff2 = b''
  for x in range(len(buff)):
    buff2 += buff[x:x + 1]
    if buff2 in lengths:
      last = buff2
    else:
      if last != -1:
        if lengths[last] != 0:
          out.write(bytes([225, 131, 144 + lengths[last] - 1]))
        else:
          out.write(bytes([32]))
        buff2 = buff2[len(last):]
        last = -1
  if last != -1:
    if lengths[last] != 0:
      out.write(bytes([225, 131, 144 + lengths[last] - 1]))
    else:
      out.write(bytes([32]))
    buff2 = buff2[len(last):]
    last = -1



parse(sys.argv[2], sys.argv[1], sys.argv[3])