import unittest
from divine_agents.author import AuthorBox


class TestAuthorBox(unittest.TestCase):
    def test_identity_storage(self):
        box = AuthorBox(name="Luka Pintari\u010d", role="Author", data={"bio": "Philosopher"})
        box.update_data({"published_works": ["APD"]})
        identity = box.get_identity()
        self.assertEqual(identity["name"], "Luka Pintari\u010d")
        self.assertIn("published_works", identity["data"])


if __name__ == "__main__":
    unittest.main()

