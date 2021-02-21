class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation
      self.val = val
      self.prev = None
      self.next = None

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    # TODO replace pass with your implementation
    self.__header = Linked_List.__Node('head')
    self.__trailer = Linked_List.__Node('tail')
    self.__header.next = self.__trailer
    self.__trailer.prev = self.__header
    self.__current = self.__header.next
    self.__size = 0

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    # TODO replace pass with your implementation
    return self.__size


  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation
    new_node = Linked_List.__Node(val)

    temp = self.__trailer.prev
    new_node.next = self.__trailer
    temp.next = new_node
    new_node.prev = temp
    self.__trailer.prev = new_node
    self.__size += 1

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.
    # TODO replace pass with your implementation
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
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation
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
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node 
    # at the specified index, but do not unlink it from 
    # the list. If the specified index is invalid, raise 
    # an IndexError exception.
    # TODO replace pass with your implementation
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
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    # TODO replace pass with your implementation.
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
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
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
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
    self.__current = self.__header.next
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation

    if self.__current is self.__trailer:
      raise StopIteration
    else:
      val = self.__current.val
      self.__current = self.__current.next
      return val

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests

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