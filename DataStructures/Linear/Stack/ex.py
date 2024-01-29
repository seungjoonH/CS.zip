class Node:
  def __init__(self, value):
      self.value = value

class Stack:
  def __init__(self, init=[]):
    self.process = True
    self._list = [Node(e) for e in init]

  def visualize(self):
    print(f'[{", ".join(str(n.value) for n in self._list)}]')

  def length(self):
    return len(self._list)

  def push(self, value):    
    self._list.append(Node(value))
    
    if self.process:
      print(f'push({value})')
      self.visualize()

  def pop(self):
    if not self._list:
      print('[ERROR] Pop failed.')
      print('Stack is Empty')
      return
    
    rm_node = self._list.pop()

    if self.process: 
      print(f'pop() = {rm_node.value}')
      self.visualize()

    return rm_node.value
  
  def peek(self):
    if not self._list:
      print('[ERROR] Peek failed.')
      print('Stack is Empty')
      return
    
    pk_node = self._list[-1]

    if self.process: 
      print(f'peek() = {pk_node.value}')

    return pk_node.value
  
def choose():
  print()
  print('== Menu ==')
  print('[0] Quit')
  print('[1] Push')
  print('[2] Pop')
  print('[3] Peek')
  print('[4] Visualize')
  print('>>', end=' ')
  return int(input())

if __name__ == '__main__':
  s = Stack()

  while ipt := choose():
    print()

    try:
      func, param = [
        ['push', 1], 
        ['pop', 0], 
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
      
      eval(f's.{func}({",".join(params)})')

    except:
      print('[ERROR] Invalid input')
      continue
