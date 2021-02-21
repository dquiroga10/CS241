import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  
  stack = Stack()
  od = [ '[' , '{' , '(']
  cd = [ ']' , '}' , ')']
  string = ''
  with open(filename) as f:
    for line in f:
      for i in range(0,len(line)):
        if line[i] in od or line[i] in cd:
          string += line[i]
      #print(string)
  for i in string:
    if i in od:
      stack.push(i)
    elif i in cd:
      popped = stack.pop()
      count = 0
      if i == ']' and popped == '[':
        count += 1
      elif i == ')' and popped == '(':
        count += 1
      elif i == '}' and popped == '{':
        count += 1
      else: 
        return False
  if len(stack) != 0:
    return False
  return True
            

if __name__ == '__main__':

  if len(sys.argv) < 2:
    
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


