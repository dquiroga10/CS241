import unittest
from Deque_Generator import get_deque, LL_DEQUE_TYPE, ARR_DEQUE_TYPE
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    # Run your tests with each deque type to ensure that
    # they behave identically.
    self.__deque = get_deque(LL_DEQUE_TYPE)
    self.__stack = Stack()
    self.__queue = Queue()

  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_
  def test_empty_deque_str(self):
  	self.assertEqual('[ ]', str(self.__deque), 'Empty list should print as "[ ]"')

  def test_deque_push_front_one(self):
  	self.__deque.push_front('Data')
  	self.assertEqual('[ Data ]', str(self.__deque))

  def test_deque_push_front_two(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.assertEqual('[ Structures, Data ]', str(self.__deque))

  def test_deque_push_back_one(self):
  	self.__deque.push_back('Data')
  	self.assertEqual('[ Data ]', str(self.__deque))

  def test_deque_push_back_two(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.assertEqual('[ Data, Structures ]', str(self.__deque))

  def test_deque_push_front_push_back(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_back('101')
  	self.assertEqual('[ Data, 101 ]', str(self.__deque))

  def test_deque_push_back_push_front(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_front('Love')
  	self.assertEqual('[ Love, Data ]', str(self.__deque))

  def test_deque_push_front_two_push_back(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.push_back('101')
  	self.assertEqual('[ Structures, Data, 101 ]', str(self.__deque))

  def test_deque_push_back_two_push_front(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.__deque.push_front('Love')
  	self.assertEqual('[ Love, Data, Structures ]', str(self.__deque))

  def test_push_front_three_pop_front_value(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.push_front('Love')
  	value = str(self.__deque.pop_front())
  	self.assertEqual('Love', value)

  def test_push_front_three_pop_front_print(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.push_front('Love')
  	self.__deque.pop_front()
  	self.assertEqual('[ Structures, Data ]', str(self.__deque))

  def test_push_front_three_pop_back_value(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.push_front('Love')
  	value = self.__deque.pop_back()
  	self.assertEqual('Data', value)

  def test_push_front_three_pop_back_print(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.push_front('Love')
  	self.__deque.pop_back()
  	self.assertEqual('[ Love, Structures ]', str(self.__deque))

  def test_push_back_three_pop_front_value(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.__deque.push_back('Love')
  	value = self.__deque.pop_front()
  	self.assertEqual('Data', value)


  def test_push_back_three_pop_front_print(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.__deque.push_back('Love')
  	self.__deque.pop_front()
  	self.assertEqual('[ Structures, Love ]', str(self.__deque))

  def test_push_back_three_pop_back_value(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.__deque.push_back('Love')
  	value = self.__deque.pop_back()
  	self.assertEqual('Love', value)

  def test_push_back_three_pop_back_print(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.__deque.push_back('Love')
  	self.__deque.pop_back()
  	self.assertEqual('[ Data, Structures ]', str(self.__deque))

  def test_push_front_three_pop_front_two_values(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.push_front('Love')
  	value = self.__deque.pop_front()
  	self.assertEqual('Love', value)
  	value1 = self.__deque.pop_front()
  	self.assertEqual('Structures', value1)


  def test_push_front_three_pop_front_two_print(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.push_front('Love')
  	self.__deque.pop_front()
  	self.__deque.pop_front()
  	self.assertEqual('[ Data ]', str(self.__deque))

  def test_push_back_three_pop_front_two_values(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.__deque.push_back('Love')
  	value = self.__deque.pop_front()
  	self.assertEqual('Data', value)
  	value1 = self.__deque.pop_front()
  	self.assertEqual('Structures', value1)

  def test_push_back_three_pop_front_two_print(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.__deque.push_back('Love')
  	self.__deque.pop_front()
  	self.__deque.pop_front()
  	self.assertEqual('[ Love ]', str(self.__deque))

  def test_push_front_three_pop_front_pop_back_values(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.push_front('Love')
  	value = self.__deque.pop_front()
  	self.assertEqual('Love', value)
  	value1 = self.__deque.pop_back()
  	self.assertEqual('Data', value1)

  def test_push_front_three_pop_front_pop_back_print(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.push_front('Love')
  	self.__deque.pop_front()
  	self.__deque.pop_back()
  	self.assertEqual('[ Structures ]', str(self.__deque))

  def test_push_back_three_pop_front_pop_back_values(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.__deque.push_back('Love')
  	value = self.__deque.pop_front()
  	self.assertEqual('Data', value)
  	value1 = self.__deque.pop_back()
  	self.assertEqual('Love', value1)

  def test_push_back_three_pop_front_pop_back_print(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.__deque.push_back('Love')
  	self.__deque.pop_front()
  	self.__deque.pop_back()
  	self.assertEqual('[ Structures ]', str(self.__deque))

  def test_push_front_three_pop_back_pop_front_values(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.push_front('Love')
  	value = self.__deque.pop_back()
  	self.assertEqual('Data', value)
  	value1 = self.__deque.pop_front()
  	self.assertEqual('Love', value1)

  def test_push_front_three_pop_back_pop_front_print(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.push_front('Love')
  	self.__deque.pop_back()
  	self.__deque.pop_front()
  	self.assertEqual('[ Structures ]', str(self.__deque))

  def test_push_back_three_pop_back_pop_front_values(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.__deque.push_back('Love')
  	value = self.__deque.pop_back()
  	self.assertEqual('Love', value)
  	value1 = self.__deque.pop_front()
  	self.assertEqual('Data', value1)
  	self.assertEqual('[ Structures ]', str(self.__deque))

  def test_push_back_three_pop_back_pop_front_print(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.__deque.push_back('Love')
  	self.__deque.pop_back()
  	self.__deque.pop_front()
  	self.assertEqual('[ Structures ]', str(self.__deque))

  def test_pop_front_empty_deque(self):
  	value = self.__deque.pop_front()
  	self.assertEqual(None, value)

  def test_pop_front_empty_deque_print(self):
  	self.__deque.pop_front()
  	self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_empty_deque_length(self):
  	self.__deque.pop_front()
  	self.assertEqual(0, len(self.__deque))

  def test_pop_back_empty_deque(self):
  	value = self.__deque.pop_back()
  	self.assertEqual(None, value)

  def test_pop_back_empty_deque_print(self):
  	self.__deque.pop_back()
  	self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_empty_deque_length(self):
  	self.__deque.pop_back()
  	self.assertEqual(0, len(self.__deque))

  def test_get_empty_length(self):
  	self.assertEqual(0, len(self.__deque))

  def test_get_empty_length_pop_front(self):
  	self.__deque.pop_front()
  	self.assertEqual(0, len(self.__deque))

  def test_get_empty_length_pop_back(self):
  	self.__deque.pop_back()
  	self.assertEqual(0, len(self.__deque))

  def test_get_one_length_push_back(self):
  	self.__deque.push_back('Data')
  	self.assertEqual(1, len(self.__deque))

  def test_get_two_length_push_back(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.assertEqual(2, len(self.__deque))

  def test_get_one_length_push_front(self):
  	self.__deque.push_front('Data')
  	self.assertEqual(1, len(self.__deque))

  def test_get_two_length_push_front(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.assertEqual(2, len(self.__deque))

  def test_get_two_length_push_back_pop_front(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.__deque.push_back('101')
  	self.__deque.pop_front()
  	self.assertEqual(2, len(self.__deque))

  def test_get_two_length_push_back_pop_back(self):
  	self.__deque.push_back('Data')
  	self.__deque.push_back('Structures')
  	self.__deque.push_back('101')
  	self.__deque.pop_back()
  	self.assertEqual(2, len(self.__deque))

  def test_get_two_length_push_front_pop_front(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.push_front('101')
  	self.__deque.pop_front()
  	self.assertEqual(2, len(self.__deque))

  def test_get_two_length_push_front_pop_back(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.push_front('101')
  	self.__deque.pop_back()
  	self.assertEqual(2, len(self.__deque))

  def test_peek_front_empty_deque(self):
  	value = self.__deque.peek_front()
  	self.assertEqual(None, value)

  def test_peek_front_empty_deque_print(self):
  	self.__deque.peek_front()
  	self.assertEqual('[ ]', str(self.__deque))

  def test_peek_front_empty_deque_length(self):
  	self.__deque.peek_front()
  	self.assertEqual(0, len(self.__deque))

  def test_peek_back_empty_deque(self):
  	value = self.__deque.peek_back()
  	self.assertEqual(None, value)

  def test_peek_back_empty_deque_print(self):
  	self.__deque.peek_back()
  	self.assertEqual('[ ]', str(self.__deque))

  def test_peek_back_empty_deque_length(self):
  	self.__deque.peek_back()
  	self.assertEqual(0, len(self.__deque))

  def test_peek_front_deque_one(self):
  	self.__deque.push_front('Data')
  	value = self.__deque.peek_front()
  	self.assertEqual('Data', value)

  def test_peek_front_deque_one_print(self):
  	self.__deque.push_front('Data')
  	self.__deque.peek_front()
  	self.assertEqual('[ Data ]', str(self.__deque))

  def test_peek_front_deque_one_length(self):
  	self.__deque.push_front('Data')
  	self.__deque.peek_front()
  	self.assertEqual(1, len(self.__deque))

  def test_peek_front_deque_two(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	value = self.__deque.peek_front()
  	self.assertEqual('Structures', value)

  def test_peek_front_deque_two_print(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.peek_front()
  	self.assertEqual('[ Structures, Data ]', str(self.__deque))

  def test_peek_front_deque_two_length(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.peek_front()
  	self.assertEqual(2, len(self.__deque))

  def test_peek_back_deque_one(self):
  	self.__deque.push_front('Data')
  	value = self.__deque.peek_back()
  	self.assertEqual('Data', value)

  def test_peek_back_deque_one_print(self):
  	self.__deque.push_front('Data')
  	self.__deque.peek_back()
  	self.assertEqual('[ Data ]', str(self.__deque))

  def test_peek_back_deque_one_length(self):
  	self.__deque.push_front('Data')
  	self.__deque.peek_back()
  	self.assertEqual(1, len(self.__deque))

  def test_peek_back_deque_two(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	value = self.__deque.peek_back()
  	self.assertEqual('Data', value)

  def test_peek_back_deque_two_print(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.peek_back()
  	self.assertEqual('[ Structures, Data ]', str(self.__deque))

  def test_peek_back_deque_two_length(self):
  	self.__deque.push_front('Data')
  	self.__deque.push_front('Structures')
  	self.__deque.peek_back()
  	self.assertEqual(2, len(self.__deque))

  def test_empty_stack_string(self):
  	self.assertEqual('[ ]', str(self.__stack))

  def test_empty_stack_length(self):
  	self.assertEqual(0, len(self.__stack))

  def test_empty_stack_pop(self):
  	value = self.__stack.pop()
  	self.assertEqual(None, value)

  def test_empty_stack_pop_print(self):
  	self.__stack.pop()
  	self.assertEqual('[ ]', str(self.__stack))

  def test_empty_stack_pop_length(self):
  	self.__stack.pop()
  	self.assertEqual(0, len(self.__stack))

  def test_stack_push_one(self):
  	self.__stack.push('Data')
  	self.assertEqual('[ Data ]', str(self.__stack))

  def test_stack_push_one_length(self):
  	self.__stack.push('Data')
  	self.assertEqual(1, len(self.__stack))

  def test_stack_push_two(self):
  	self.__stack.push('Data')
  	self.__stack.push('Structures')
  	self.assertEqual('[ Structures, Data ]', str(self.__stack))

  def test_stack_push_two_length(self):
  	self.__stack.push('Data')
  	self.__stack.push('Structures')
  	self.assertEqual(2, len(self.__stack))

  def test_stack_one_pop_value(self):
  	self.__stack.push('Data')
  	value = self.__stack.pop()
  	self.assertEqual('Data', value)

  def test_stack_one_pop_print(self):
  	self.__stack.push('Data')
  	self.__stack.pop()
  	self.assertEqual('[ ]', str(self.__stack))

  def test_stack_one_pop_length(self):
  	self.__stack.push('Data')
  	self.__stack.pop()
  	self.assertEqual(0, len(self.__stack))

  def test_stack_two_pop_value(self):
  	self.__stack.push('Data')
  	self.__stack.push('Love')
  	value = self.__stack.pop()
  	self.assertEqual('Love', value)

  def test_stack_two_pop_print(self):
  	self.__stack.push('Data')
  	self.__stack.push('Love')
  	self.__stack.pop()
  	self.assertEqual('[ Data ]', str(self.__stack))

  def test_stack_two_pop_length(self):
  	self.__stack.push('Data')
  	self.__stack.push('Love')
  	self.__stack.pop()
  	self.assertEqual(1, len(self.__stack))

  def test_stack_empty_peek_value(self):
  	value = self.__stack.peek()
  	self.assertEqual(None, value)

  def test_stack_empty_peek_print(self):
  	self.__stack.peek()
  	self.assertEqual('[ ]', str(self.__stack))

  def test_stack_empty_peek_length(self):
  	self.__stack.peek()
  	self.assertEqual(0, len(self.__stack))

  def test_stack_one_peek_value(self):
  	self.__stack.push('Data')
  	value = self.__stack.peek()
  	self.assertEqual('Data' , value)

  def test_stack_one_peek_print(self):
  	self.__stack.push('Data')
  	self.__stack.peek()
  	self.assertEqual('[ Data ]', str(self.__stack))

  def test_stack_one_peek_length(self):
  	self.__stack.push('Data')
  	self.__stack.peek()
  	self.assertEqual(1, len(self.__stack))

  def test_stack_two_peek_value(self):
  	self.__stack.push('Data')
  	self.__stack.push('Structures')
  	value = self.__stack.peek()
  	self.assertEqual('Structures' , value)

  def test_stack_two_peek_print(self):
  	self.__stack.push('Data')
  	self.__stack.push('Structures')
  	self.__stack.peek()
  	self.assertEqual('[ Structures, Data ]', str(self.__stack))

  def test_stack_two_peek_length(self):
  	self.__stack.push('Data')
  	self.__stack.push('Structures')
  	self.__stack.peek()
  	self.assertEqual(2, len(self.__stack))

  def test_enqueue_empty_queue(self):
  	self.__queue.enqueue('Data')
  	self.assertEqual('[ Data ]', str(self.__queue))

  def test_enqueue_empty_queue_length(self):
  	self.__queue.enqueue('Data')
  	self.assertEqual(1, len(self.__queue))

  def test_dequeue_empty_queue(self):
  	self.__queue.dequeue()
  	self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_empty_queue_value(self):
  	value = self.__queue.dequeue()
  	self.assertEqual(None, value)

  def test_dequeue_empty_queue_length(self):
  	self.__queue.dequeue()
  	self.assertEqual(0, len(self.__queue))

  def test_enqueue_one_queue(self):
  	self.__queue.enqueue('Data')
  	self.__queue.enqueue('Structures')
  	self.assertEqual('[ Data, Structures ]', str(self.__queue))

  def test_enqueue_one_queue_length(self):
  	self.__queue.enqueue('Data')
  	self.__queue.enqueue('Structures')
  	self.assertEqual(2, len(self.__queue))

  def test_dequeue_one_queue(self):
  	self.__queue.enqueue('Data')
  	self.__queue.dequeue()
  	self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_one_queue_value(self):
  	self.__queue.enqueue('Data')
  	value = self.__queue.dequeue()
  	self.assertEqual('Data', value)

  def test_dequeue_one_queue_length(self):
  	self.__queue.enqueue('Data')
  	self.__queue.dequeue()
  	self.assertEqual(0, len(self.__queue))

  def test_dequeue_two_queue(self):
  	self.__queue.enqueue('Data')
  	self.__queue.enqueue('Structures')
  	self.__queue.dequeue()
  	self.assertEqual('[ Structures ]', str(self.__queue))

  def test_dequeue_two_queue_value(self):
  	self.__queue.enqueue('Data')
  	self.__queue.enqueue('Structures')
  	value = self.__queue.dequeue()
  	self.assertEqual('Data', value)

  def test_dequeue_two_queue_length(self):
  	self.__queue.enqueue('Data')
  	self.__queue.enqueue('Structures')
  	self.__queue.dequeue()
  	self.assertEqual(1, len(self.__queue))

  def test_dequeue_three_queue(self):
  	self.__queue.enqueue('Data')
  	self.__queue.enqueue('Structures')
  	self.__queue.enqueue('101')
  	self.__queue.dequeue()
  	self.assertEqual('[ Structures, 101 ]', str(self.__queue))

  def test_dequeue_three_queue_value(self):
  	self.__queue.enqueue('Data')
  	self.__queue.enqueue('Structures')
  	self.__queue.enqueue('101')
  	value = self.__queue.dequeue()
  	self.assertEqual('Data', value)

  def test_dequeue_three_queue_length(self):
  	self.__queue.enqueue('Data')
  	self.__queue.enqueue('Structures')
  	self.__queue.enqueue('101')
  	self.__queue.dequeue()
  	self.assertEqual(2, len(self.__queue))

  def test_deque_push_front_NONE(self):
    with self.assertRaises(ValueError):
      self.__deque.push_front(None)
    self.assertEqual('[ ]', str(self.__deque))

  def test_deque_push_front_NONE_length(self):
    with self.assertRaises(ValueError):
      self.__deque.push_front(None)
    self.assertEqual(0, len(self.__deque))

  def test_deque_push_back_NONE(self):
    with self.assertRaises(ValueError):
      self.__deque.push_back(None)
    self.assertEqual('[ ]', str(self.__deque))

  def test_deque_push_back_NONE_length(self):
    with self.assertRaises(ValueError):
      self.__deque.push_back(None)
    self.assertEqual(0, len(self.__deque))


if __name__ == '__main__':
  unittest.main()

