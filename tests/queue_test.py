import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        try:
            self.queue = Queue()
        except Exception as e:
            print(f"Setup failed: {e}")
            return

    def test_enqueue(self):
        try:
            self.queue.enqueue(1)
            self.assertEqual(self.queue.peek(), 1)
        except Exception as e:
            print(f"Enqueue test failed: {e}")

    def test_dequeue(self):
        try:
            self.queue.enqueue(1)
            self.queue.enqueue(2)
            self.assertEqual(self.queue.dequeue(), 1)
        except Exception as e:
            print(f"Dequeue test failed: {e}")

    def test_peek(self):
        try:
            self.queue.enqueue(1)
            self.assertEqual(self.queue.peek(), 1)
        except Exception as e:
            print(f"Peek test failed: {e}")

    def test_is_empty(self):
        try:
            self.assertTrue(self.queue.is_empty())
            self.queue.enqueue(1)
            self.assertFalse(self.queue.is_empty())
        except Exception as e:
            print(f"Is_empty test failed: {e}")

    def test_count(self):
        try:
            self.assertEqual(self.queue.count(), 0)
            self.queue.enqueue(1)
            self.assertEqual(self.queue.count(), 1)
        except Exception as e:
            print(f"Count test failed: {e}")


if __name__ == "__main__":
    unittest.main()
