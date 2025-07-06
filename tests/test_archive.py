import unittest
from divine_agents.archive import Archive, Contact
from divine_agents.library import Library


class TestArchive(unittest.TestCase):
    def test_reorganize(self):
        archive = Archive()
        archive.add_contact(Contact("A", "B", "event1", "2"))
        archive.add_contact(Contact("B", "A", "event2", "1"))
        archive.reorganize()
        self.assertEqual([c.timestamp for c in archive], ["1", "2"])

    def test_library_average(self):
        archive = Archive()
        archive.add_contact(Contact("A", "B", "event1", "1"))
        archive.add_contact(Contact("B", "A", "event2", "3"))
        lib = Library(archive)
        self.assertAlmostEqual(lib.average_contact_interval(), 2.0)

if __name__ == "__main__":
    unittest.main()
