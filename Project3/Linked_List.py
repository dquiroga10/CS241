class Linked_List:
  
  class __Node:
    
    def __init__(self, val):

      self.val = val
      self.prev = None
      self.next = None

  def __init__(self):

    self.__header = Linked_List.__Node('head')
    self.__trailer = Linked_List.__Node('tail')
    self.__header.next = self.__trailer
    self.__trailer.prev = self.__header
    self.__current = self.__header.next
    self.__size = 0

  def __len__(self):

    return self.__size


  def append_element(self, val):

    new_node = Linked_List.__Node(val)

    temp = self.__trailer.prev
    new_node.next = self.__trailer
    temp.next = new_node
    new_node.prev = temp
    self.__trailer.prev = new_node
    self.__size += 1

  def insert_element_at(self, val, index):

    new_node = Linked_List.__Node(val)
    temp = self.__header
    count = 0

    if index > self.__size-1 or index < 0:
      raise IndexError
    else: 
      while count < index:
        temp = temp.next
        count += 1
      new_node.next = temp.next
      cur1 = temp.next
      cur1.prev = new_node 
      temp.next = new_node
      new_node.prev = temp
      self.__size += 1


  def remove_element_at(self, index):

    temp = self.__header
    count = 0
    node_val = None

    if index >= self.__size or index < 0:
      raise IndexError
    else: 
      while count < index: 
        temp = temp.next
        count += 1
      node_val = temp.next.val
      node = temp.next
      temp.next = node.next
      cur1 = node.next
      cur1.prev = temp

      self.__size -= 1
    return node_val

  def get_element_at(self, index):

    temp = self.__header.next
    count = 0
    node_val = None

    if index >= self.__size or index < 0:
      raise IndexError
    else: 
      while count < index:
        temp = temp.next
        count += 1
      node_val = temp.val
    return node_val

  def rotate_left(self):

    temp = self.__header.next

    if temp.next is not self.__trailer and temp is not self.__trailer:
      self.__header.next = temp.next
      temp.next.prev = self.__header
      temp.next = self.__trailer
      temp.prev = self.__trailer.prev
      self.__trailer.prev.next = temp
      self.__trailer.prev = temp
    else:
      temp = self.__header
    
  def __str__(self):

    if self.__size == 0:
      ll = '[ ]'
    else:
      ll = '['
      temp = self.__header
      while temp.next is not self.__trailer:
        ll += ' '+ str(temp.next.val) + ','
        temp = temp.next
      ll = ll[0:len(ll) - 1]
      ll += ' ]'
    return ll

  def __iter__(self):

    self.__current = self.__header.next
    return self

  def __next__(self):

    if self.__current is self.__trailer:
      raise StopIteration
    else:
      val = self.__current.val
      self.__current = self.__current.next
      return val

if __name__ == '__main__':

  #test case for appending elements and making sure the size is right
  ll1 = Linked_List()
  print('L-List 1:', ll1.__str__())
  print('len:', ll1.__len__())
  ll1.append_element(5)
  print('L-List 1:', ll1.__str__())
  print('len:', ll1.__len__())
  ll1.append_element(4)
  print('L-List 1:', ll1.__str__())
  print('len:', ll1.__len__())
  ll1.append_element(-54)
  print('L-List 1:', ll1.__str__())
  print('len:', ll1.__len__())
  ll1.append_element(21)
  print('L-List 1:', ll1.__str__())
  print('len:', ll1.__len__())
  #for loop visits every value
  for val in ll1:
    print(val)
  print('----------------------------------------------------------------------')

  #test case for empty list insert and then regular insert//check len function working properly
  ll2 = Linked_List()
  ll2.insert_element_at(5,0)#invalid-empty linked list
  ll2.append_element(3)#creating a linked list
  ll2.append_element(6)
  ll2.append_element(83)
  ll2.append_element(43)
  ll2.append_element(93)
  ll2.append_element(24)
  ll2.append_element(87)
  ll2.append_element(100)
  ll2.append_element(32)
  print('L-List2:', ll2.__str__())
  print('len:',ll2.__len__())
  ll2.insert_element_at(5,5)#valid  
  print('updated L-List2:',ll2.__str__())
  print('new len:',ll2.__len__())
  #no change when invalid index is added
  ll2.insert_element_at(55, -1)#invalid
  print(ll2.__str__())
  print('len:',ll2.__len__())
  ll2.insert_element_at(55,10)#invalid
  print(ll2.__str__())
  print('len:',ll2.__len__())
  #for loop visits every value
  for val in ll2:
    print(val)
  print('----------------------------------------------------------------------')

#test case for removing at a valid and invalid index
  ll3 = Linked_List()
  ll3.remove_element_at(0)#invalid
  ll3.append_element(3)#creating a linked list
  ll3.append_element(6)
  ll3.append_element(83)
  ll3.append_element(43)
  ll3.append_element(93)
  ll3.append_element(24)
  ll3.append_element(87)
  ll3.append_element(100)
  ll3.append_element(32)
  ll3.append_element(54)
  ll3.append_element(93)
  ll3.append_element(121)
  ll3.append_element(82)
  print('L-List3:', ll3.__str__())
  print('new len:',ll3.__len__())
  print('val removed:',ll3.remove_element_at(13))#invalid
  print(ll3.__str__())
  print('len:',ll3.__len__())
  print('val removed:',ll3.remove_element_at(-1))#invalid
  print(ll3.__str__())
  print('new len:',ll3.__len__())
  print('val removed:',ll3.remove_element_at(12))#valid-prints value that is being removed
  print('updated L-List3:',ll3.__str__())#prints the list after the value has been removed
  print('new len:',ll3.__len__())#prints the change of length after the removal
  #test case to see if for loop visits every value left in ll3
  for val in ll3:
    print(val)
  print('----------------------------------------------------------------------')

#test case for string representation works for every size and length also works properly
  ll4 = Linked_List()
  count = 0
  while count < 50:
    ll4.append_element(count)
    count += 1
  print('L-List4:',ll4.__str__())
  print('len:',ll4.__len__())
  #test case for get element 
  print('val:',ll4.get_element_at(49))#valid
  print('val:',ll4.get_element_at(0))#valid
  print('val:',ll4.get_element_at(-1))#invalid
  print('val:',ll4.get_element_at(50))#invalid
  print('L-List4:', ll4.__str__())
  print('len:', ll4.__len__())