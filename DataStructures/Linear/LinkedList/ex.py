class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.process = True
    self.head = None

  def visualize(self):
    link = self.head

    while link:
      print(link.value, end='')
      link = link.next
      print(' > ', end='')

    print('NULL\n')

  def length(self):
    link, count = self.head, 0
    while link: 
      link = link.next
      count += 1
    return count

  def add(self, value):
    if self.process: 
      print(f'add({value})')

    node = Node(value)

    if self.head:
      cur = self.head
      temp = None

      while cur:
        temp = cur
        cur = cur.next

      temp.next = node

    else:
      self.head = node

    if self.process: 
      self.visualize()

  def insert(self, index, value):
    if not (0 <= index < self.length()):
      print('[ERROR] Insert failed.')
      print(f'Index out of range: 0 ~ {self.length()} but "{index}"\n')
      return

    if self.process: 
      print(f'insert({index}, {value})')

    node = Node(value)
    cur = self.head

    if index == 0:
      node.next = cur
      self.head = node

    elif index == self.length() - 1:
      self.add(value)
      return

    for count in range(1, self.length()):
      if index == count:
        node.next = cur.next
        cur.next = node
        break

      cur = cur.next

    if self.process:
      self.visualize()

  def pop(self):
    if not self.head:
      print('[ERROR] Pop failed.')
      print('List is Empty')
      return
    
    print('pop()', end=' = ')

    rm_node = None
    cur = self.head

    while cur:
      if not cur.next:
        rm_node = self.head
        self.head = None
        break

      if not cur.next.next:
        rm_node = cur.next
        cur.next = None
        break

      cur = cur.next
    
    print(rm_node.value)

    if self.process: 
      self.visualize()

  def remove(self, index):
    if not self.head:
      print('[ERROR] Remove failed.')
      print('List is Empty')
      return
    
    if not (0 <= index < self.length()):
      print('[ERROR] Remove failed.')
      print(f'Index out of range: 0 ~ {self.length()} but "{index}"\n')
      return

    print(f'remove({index})', end=' = ')

    rm_node = None
    cur = self.head

    if index == 0:
      rm_node = cur
      self.head = cur.next

    elif index == self.length() - 1:
      self.pop()
      return

    for count in range(1, self.length()):
      if index == count:
        rm_node = cur.next
        cur.next = cur.next.next
        break

      cur = cur.next

    print(rm_node.value)

    if self.process: 
      self.visualize()

    return rm_node.value
  
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
