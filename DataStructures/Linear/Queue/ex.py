class Node:
  def __init__(self, value):
      self.value = value

class Queue:
  def __init__(self, init=[]):
    self.process = True
    self._list = [Node(e) for e in init]

  def visualize(self):
    print(f'[{", ".join(str(n.value) for n in self._list)}]')

  def length(self):
    return len(self._list)

  def enqueue(self, value):    
    self._list.append(Node(value))
    
    if self.process:
      print(f'enqueue({value})')
      self.visualize()

  def dequeue(self):
    if not self._list:
      print('[ERROR] Dequeue failed.')
      print('Queue is Empty')
      return
    
    rm_node = self._list.pop(0)

    if self.process: 
      print(f'dequeue() = {rm_node.value}')
      self.visualize()

    return rm_node.value
  
  def peek(self):
    if not self._list:
      print('[ERROR] Peek failed.')
      print('Stack is Empty')
      return
    
    pk_node = self._list[0]

    if self.process: 
      print(f'peek() = {pk_node.value}')

    return pk_node.value
  
def choose():
  print()
  print('== Menu ==')
  print('[0] Quit')
  print('[1] Enqueue')
  print('[2] Dequeue')
  print('[3] Peek')
  print('[4] Visualize')
  print('>>', end=' ')
  return int(input())

if __name__ == '__main__':
  q = Queue()

  while ipt := choose():
    print()

    try:
      func, param = [
        ['enqueue', 1], 
        ['dequeue', 0], 
        ['peek', 0],
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
      
      eval(f'q.{func}({",".join(params)})')

    except:
      print('[ERROR] Invalid input')
      continue
