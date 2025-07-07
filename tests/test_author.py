import unittest
from divine_agents.author import AuthorBox


class TestAuthorBox(unittest.TestCase):
    def test_initial_identity(self):
        box = AuthorBox("Luka Pintari\u010d", role="Author")
        identity = box.get_identity()
        self.assertEqual(identity["name"], "Luka Pintari\u010d")
        self.assertEqual(identity["role"], "Author")
        self.assertIn("identity", identity["data"])  # default data

    def test_update_data(self):
        box = AuthorBox("Luka")
        box.update_data({"works": ["APD"]})
        self.assertIn("works", box.data)
        self.assertEqual(box.data["works"], ["APD"])


if __name__ == "__main__":
    unittest.main()
