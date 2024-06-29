import unittest
from hash_map.hash_map import HashMap


class TestHashMap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert hasattr(
            HashMap, "HashMap"
        ), "The HashMap class is not defined in the hash_map module"
        return

    def test_insert(self):
        hash_map = HashMap()
        hash_map.insert("key", "value")
        hash_map.insert("key2", "value2")
        self.assertEqual(hash_map.get("key"), "value")
        self.assertEqual(hash_map.get("key2"), "value2")


if __name__ == "__main__":
    unittest.main()
