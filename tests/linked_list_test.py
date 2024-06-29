import unittest
from linked_list.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert hasattr(
            LinkedList, "LinkedList"
        ), "The LinkedList class is not defined in the linked_list module"
        return

    def test_insert_at_head(self):
        linked_list = LinkedList()
        linked_list.insert_at_head(1)
        self.assertEqual(linked_list.head.data, 1)

    def test_insert_at_tail(self):
        linked_list = LinkedList()
        linked_list.insert_at_tail(1)
        self.assertEqual(linked_list.head.data, 1)

    def test_update_node(self):
        linked_list = LinkedList()
        linked_list.insert_at_head(1)
        linked_list.update_node(1, 2)
        self.assertEqual(linked_list.head.data, 2)

    def test_delete_head(self):
        linked_list = LinkedList()
        linked_list.insert_at_head(1)
        linked_list.delete_head()
        self.assertEqual(linked_list.head, None)

    def test_delete_tail(self):
        linked_list = LinkedList()
        linked_list.insert_at_head(1)
        linked_list.delete_tail()
        self.assertEqual(linked_list.head, None)

    def test_get_node(self):
        linked_list = LinkedList()
        linked_list.insert_at_head(1)
        self.assertEqual(linked_list.get_node(1).data, 1)
        linked_list.insert_at_head(2)
        self.assertEqual(linked_list.get_node(2).data, 2)


if __name__ == "__main__":
    unittest.main()
