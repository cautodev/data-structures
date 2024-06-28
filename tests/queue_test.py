import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        return

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)

    def test_peek(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())

    def test_count(self):
        self.assertEqual(self.queue.count(), 0)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.count(), 1)


if __name__ == "__main__":
    unittest.main()
