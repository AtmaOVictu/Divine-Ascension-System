import unittest
from datetime import datetime, timedelta

from divine_agents.archive import Arhiv, Stik, Library


class TestArchive(unittest.TestCase):
    def test_add_and_reorganize(self):
        arhiv = Arhiv()
        t1 = datetime.now()
        t2 = t1 + timedelta(seconds=10)
        arhiv.add_stik(Stik("A", "B", "dogodek1", t2))
        arhiv.add_stik(Stik("B", "C", "dogodek2", t1))
        arhiv.reorganize()
        descriptions = arhiv.display()
        self.assertTrue(descriptions[0].startswith("Stik med B"))

    def test_library_analysis(self):
        arhiv = Arhiv()
        now = datetime.now()
        arhiv.add_stik(Stik("A", "B", "dogodek1", now))
        arhiv.add_stik(Stik("B", "C", "dogodek2", now + timedelta(seconds=5)))
        lib = Library(arhiv)
        self.assertEqual(lib.count_contacts(), 2)
        avg = lib.average_time_between()
        self.assertAlmostEqual(avg, 5.0, places=2)


if __name__ == "__main__":
    unittest.main()
