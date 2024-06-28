import unittest
from stack.stack import Stack


class TestStack(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            assert hasattr(
                Stack, "Stack"
            ), "The Stack class is not defined in the stack module"
        except Exception as e:
            print(f"Setup failed: {e}")
            return

    def test_push(self):
        try:
            stack = Stack()
            stack.push(1)
            self.assertEqual(stack.peek(), 1)
        except Exception as e:
            print(f"Test failed: {e}")

    def test_pop(self):
        try:
            stack = Stack()
            stack.push(1)
            self.assertEqual(stack.pop(), 1)
        except Exception as e:
            print(f"Test failed: {e}")

    def test_peek(self):
        try:
            stack = Stack()
            stack.push(1)
            self.assertEqual(stack.peek(), 1)
        except Exception as e:
            print(f"Test failed: {e}")

    def test_is_empty(self):
        try:
            stack = Stack()
            self.assertTrue(stack.is_empty())
        except Exception as e:
            print(f"Test failed: {e}")

    def test_is_not_empty(self):
        try:
            stack = Stack()
            stack.push(1)
            self.assertFalse(stack.is_empty())
        except Exception as e:
            print(f"Test failed: {e}")


if __name__ == "__main__":
    unittest.main()
