import unittest
from datetime import datetime, timedelta

from divine_agents.archive import Archive, Contact
from divine_agents.library import Library


class TestArchive(unittest.TestCase):
    def test_reorganize(self):
        archive = Archive()
        older = datetime.now()
        newer = older + timedelta(hours=1)
        c1 = Contact("A", "B", "e1", newer)
        c2 = Contact("B", "C", "e2", older)
        archive.add_contact(c1)
        archive.add_contact(c2)
        archive.reorganize()
        self.assertEqual(list(archive)[0], c2)

    def test_average_time(self):
        archive = Archive()
        t1 = datetime(2024, 1, 1, 12, 0, 0)
        t2 = t1 + timedelta(minutes=30)
        t3 = t2 + timedelta(minutes=30)
        library = Library(archive)
        library.record_contact("A", "B", "e1", t1)
        library.record_contact("B", "C", "e2", t2)
        library.record_contact("C", "D", "e3", t3)
        avg = library.average_time_between_contacts()
        self.assertAlmostEqual(avg, 1800.0, delta=1)


if __name__ == "__main__":
    unittest.main()
