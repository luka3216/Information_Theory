import sys
import math

def getRepresentativeMap(encodingTree, bitMap, soFar):
  if encodingTree is None:
    return
	
  if (encodingTree["c"] is not None):
    bitMap.append((encodingTree["c"], soFar))
  soFar += '0'
  getRepresentativeMap(encodingTree["left"], bitMap, soFar)
  soFar = list(soFar)
  soFar[len(soFar) - 1] = '1'
  soFar = "".join(soFar)
  getRepresentativeMap(encodingTree["right"], bitMap, soFar)
  soFar = soFar[:-1]

def heappop(queue):
  p = 1.2
  res = None
  for x in queue:
    if x["p"] < p:
      p = x["p"]
      res = x
  queue.remove(res)
  return res

def huffman(p):
  queue = []
  for x in p:
    newnode = {"p": p[x], "c": x, "left": None, "right":None}
    queue.append(newnode)
  while (len(queue) > 1):
    node1 = heappop(queue)
    node2 = heappop(queue)
    newnode = {"p": node1["p"] + node2["p"], "c": None, "left": node1, "right": node2}
    queue.append(newnode)
  return queue[0]

def bitpop(queue):
  p = 100000
  res = None
  for x in queue:
    if x[0] < p:
      p = x[0]
      res = x
  queue.remove(res)
  return res

def heapsort(iterable):
  h = []
  for value in iterable:
    h.append(value)
  return [bitpop(h) for i in range(len(h))]

def parse(fromF, toF):
  file = open(fromF, 'rb')
  out = open(toF, 'w')
  size = int(file.readline())
  lengths = dict(zip([x for x in range(size)], [float(x) for x in file.readline().split()]))
  tree = huffman(lengths)
  bitmap = []
  getRepresentativeMap(tree, bitmap, "")
  sum = 0.0
  bitmap = heapsort(bitmap)
  for x in bitmap:
    sum += len(x[1]) * lengths[x[0]]
    out.write(x[1] + " ")
  



parse(sys.argv[1], sys.argv[2])