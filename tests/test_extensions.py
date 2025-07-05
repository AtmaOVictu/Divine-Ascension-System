import unittest
from divine_agents.extensions import (
    Samoregulacija,
    VecDimenzionalniAgent,
    Ucenje,
    CustvenaDinamika,
)


class TestExtensions(unittest.TestCase):
    def test_samoregulacija(self):
        sam = Samoregulacija(energija=10.0, napetost=0.9)
        sam.prilagodi()
        self.assertEqual(sam.energija, 5.0)

    def test_vec_dimenzionalni_agent(self):
        agent = VecDimenzionalniAgent("A")
        dim = agent.prehod_v_dimenzijo()
        self.assertEqual(dim, 2)

    def test_ucenje(self):
        u = Ucenje()
        for i in range(6):
            u.uci(f"exp{i}")
        self.assertTrue(u.optimiziraj_odlocitve())

    def test_custvena_dinamika(self):
        c = CustvenaDinamika()
        c.posodobi_stanje("tesnoba")
        self.assertFalse(c.eticna_presoja())


if __name__ == "__main__":
    unittest.main()

