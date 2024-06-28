import unittest
from stack.stack import Stack


class TestStack(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert hasattr(
            Stack, "Stack"
        ), "The Stack class is not defined in the stack module"
        return

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_is_not_empty(self):
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.is_empty())


if __name__ == "__main__":
    unittest.main()
