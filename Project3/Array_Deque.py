from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):

    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__size = 0
    self.__front = 0
    
  def __str__(self):
    
    arr_print = [None] * self.__size
    val = self.__front
    for i in range(self.__size):
      if self.__contents[val] != None:
        arr_print[i] = self.__contents[val]
      val = (val+1) % len(self.__contents)

    if self.__size == 0:
      AD = '[ ]'
    else:
      AD = '['
      for i in range(0,self.__size):
        AD += ' ' + str(arr_print[i]) + ','
      AD = AD[0:len(AD) - 1]
      AD += ' ]'
    return AD
    
  def __len__(self):

    return self.__size

  def __grow(self):

    start = self.__contents
    self.__capacity *= 2
    self.__contents = [None] * (self.__capacity)
    val = self.__front
    for i in range(self.__size):
      self.__contents[i] = start[val]
      val = (val+1) % len(start)
    self.__front = 0
    
  def push_front(self, val):

    if self.__size == self.__capacity:
      self.__grow()
    if val == None:
      raise ValueError
    self.__front = (self.__front-1) % self.__capacity
    self.__contents[self.__front] = val
    self.__size += 1

    
  def pop_front(self):
    
    if self.__size > 0:
      val = self.__contents[self.__front]
      self.__contents[self.__front] = None
      self.__front = (self.__front+1) % self.__capacity
      self.__size -= 1
    else:
      val = None
    return val

  def peek_front(self):

    if self.__size >= 0:
      val = self.__contents[self.__front]
    else:
      val = None
    return val
    
  def push_back(self, val):

    if self.__size == self.__capacity:
      self.__grow()
    if val == None:
      raise ValueError
    end = (self.__size + self.__front) % self.__capacity
    self.__contents[end] = val 
    self.__size += 1
  
  def pop_back(self):
    
    if self.__size > 0:
      end = (self.__size + self.__front -1) % self.__capacity
      val = self.__contents[end]
      self.__contents[end] = None
      self.__size -= 1
    else:
      val = None
    return val

  def peek_back(self):
 
    if self.__size >= 0:
      end = (self.__size + self.__front -1) % self.__capacity
      val = self.__contents[end]
    else:
      val = None
    return val

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
