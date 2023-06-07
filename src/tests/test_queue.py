import unittest
from search import Priority_queue

class Test_Queue(unittest.TestCase):

    def test_priority(self):
        list = Priority_queue()
        list.add_node((3,"node"))
        list.add_node((1,"node"))
        list.add_node((2,"node"))
        list.add_node((4,"node"))

        ans_list = [((1,"node")),((3,"node")),((2,"node")),((4,"node"))]

        self.assertEqual(list.queue, ans_list)

        list.take_node()

        ans_list = [((2,"node")),((3,"node")),((4,"node"))]

        self.assertEqual(list.queue, ans_list)
    
    def test_take_node(self):
        list = Priority_queue()
        list.queue = [(4,"node")]
        list.take_node()

        self.assertEqual(list.queue, [])