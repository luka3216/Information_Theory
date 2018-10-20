import sys
import math
import struct

def decode(buff):
  return int(buff, 2).to_bytes(len(buff) // 8, byteorder='big')

def parse(fromF, codeF, toF):
  file = open(fromF, 'rb')
  code = open(codeF, 'rb')
  out = open(toF, 'wb')
  lengths = [code.readline().strip() for x in range(34)]
  buff = b''
  while 1:
    byte = file.read(1)
    index = 0
    if byte == b'':
      break
    if byte[0] == 32:
      buff += lengths[0]
      index = 0
    else:
      file.read(1)
      byte = file.read(1)
      index = 1 + byte[0] - 144
      buff += lengths[index]
    while len(buff) >= 8:
      out.write(decode(buff[:8]))
      buff = buff[8:]
  buff = buff  + b'1'
  while len(buff) != 8:
    buff += b'0'
  out.write(decode(buff))



parse(sys.argv[2], sys.argv[1], sys.argv[3])