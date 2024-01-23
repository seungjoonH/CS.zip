class Node:
  def __init__(self, data):
    self.data = data
    self.link = None

class LinkedList:
  def __init__(self):
    self.process = True
    self.length = 0
    self.root = None

  def visualize(self):
    link = self.root

    while link:
      print(link.data, end='')
      link = link.link
      print(' > ', end='')

    print('NULL\n')


  def add(self, data):
    if self.process: 
      print(f'add({data})')

    node = Node(data)

    if self.root:
      cur = self.root
      temp = None

      while cur:
        temp = cur
        cur = cur.link

      temp.link = node

    else:
      self.root = node

    self.length += 1

    if self.process: 
      self.visualize()

  def insert(self, index, data):
    if not (0 <= index < self.length):
      print('[ERROR] Insert failed.')
      print(f'Index out of range: 0 ~ {self.length} but "{index}"\n')
      return

    if self.process: 
      print(f'insert({index}, {data})')

    node = Node(data)
    cur = self.root

    if index == 0:
      node.link = cur
      self.root = node

    elif index == self.length - 1:
      self.add(data)
      return

    for count in range(1, self.length):
      if index == count:
        node.link = cur.link
        cur.link = node
        break

      cur = cur.link
    
    self.length += 1

    if self.process:
      self.visualize()

  def pop(self):
    if self.process: 
      print('pop()', end=' = ')

    rm_node = None
    cur = self.root

    while cur:
      if not cur.link:
        rm_node = self.root
        self.root = None
        break

      if not cur.link.link:
        rm_node = cur.link
        cur.link = None
        break

      cur = cur.link

    self.length -= 1
    
    if self.process: 
      print(rm_node.data)
      self.visualize()

  def remove(self, index):
    if not (0 <= index < self.length):
      print('[ERROR] Remove failed.')
      print(f'Index out of range: 0 ~ {self.length} but "{index}"\n')
      return

    if self.process: 
      print(f'remove({index})', end=' = ')

    rm_node = None
    cur = self.root

    if index == 0:
      rm_node = cur
      self.root = cur.link

    elif index == self.length - 1:
      self.pop()
      return

    for count in range(1, self.length):
      if index == count:
        rm_node = cur.link
        cur.link = cur.link.link
        break

      cur = cur.link
    
    self.length -= 1

    if self.process: 
      print(rm_node.data)
      self.visualize()

    return rm_node.data
  
def choose():
  print()
  print('== Menu ==')
  print('[0] Quit')
  print('[1] Add')
  print('[2] Insert')
  print('[3] Pop')
  print('[4] Remove')
  print('[5] Visualize')
  print('>>', end=' ')
  return int(input())

if __name__ == '__main__':
  l = LinkedList()

  while ipt := choose():
    print()

    try:
      func, param = [
        ['add', 1], 
        ['insert', 2], 
        ['pop', 0], 
        ['remove', 1],
        ['visualize', 0],
      ][ipt - 1]
      print(f'{func}(param={param})')
      
      params = []
      if param: 
        print('>>', end=' ')
        params = input().split()
        print()

        if len(params) != param:
          print('[ERROR] Invalid input')
          continue
      
      eval(f'l.{func}({",".join(params)})')

    except:
      print('[ERROR] Invalid input')
      continue
