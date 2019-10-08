import unittest
import sistemaCuantico as sis


class prueba_simuladorCuantico(unittest.TestCase):
    def test_modulo(self):
        self.assertEqual(sis.detectParticle([(1,2),(4,5),(3,3),(1,-4),(-5,-5)],2),0.13740458015267173)
        self.assertEqual(sis.probaTransitarVector([(1,2),(4,5),(3,3),(1,-4),(-5,-5)],[(-1,2),(4,-5),(-3,3),(-1,4),(5,5)]),(-0.25190839694656486, 0.32061068702290074))


if __name__ == "__main__":
    unittest.main()

