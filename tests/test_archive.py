import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.archive import Contact, Archive, Library


class TestArchive(unittest.TestCase):
    def test_reorganize(self):
        archive = Archive()
        c1 = Contact("A", "B", "e1", 2)
        c2 = Contact("B", "C", "e2", 1)
        archive.add_contact(c1)
        archive.add_contact(c2)
        archive.reorganize()
        contacts = archive.get_contacts()
        self.assertEqual(contacts[0], c2)
        self.assertEqual(contacts[1], c1)

    def test_library_average(self):
        archive = Archive()
        archive.add_contact(Contact("A", "B", "e1", 1))
        archive.add_contact(Contact("B", "C", "e2", 3))
        lib = Library(archive)
        self.assertEqual(lib.average_timestamp(), 2)


if __name__ == '__main__':
    unittest.main()
