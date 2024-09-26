import unittest
from app.clases import Aluminio, Vidrio, Ventana, Cotizacion, Cliente

class TestAluminio(unittest.TestCase):
    def test_aluminio_precio(self):
        aluminio_pulido = Aluminio("Pulido", 50700)
        self.assertEqual(aluminio_pulido.precio, 50700)

class TestVidrio(unittest.TestCase):
    def test_vidrio_precio(self):
        vidrio_transparente = Vidrio("Transparente", 8.25)
        self.assertEqual(vidrio_transparente.precio, 8.25)

    def test_vidrio_con_esmerilado(self):
        vidrio_bronce = Vidrio("Bronce", 9.15, esmerilado=True)
        self.assertEqual(vidrio_bronce.precio, 9.15)
        self.assertTrue(vidrio_bronce.esmerilado)

class TestVentana(unittest.TestCase):
    def test_calcular_costo_ventana(self):
        aluminio_pulido = Aluminio("Pulido", 50700)
        vidrio_transparente = Vidrio("Transparente", 8.25)
        ventana = Ventana("O", 120, 90, aluminio_pulido, vidrio_transparente, 1)

        costo_total_esperado = ventana.calcular_costo_ventana()
        self.assertTrue(costo_total_esperado > 0)

class TestCotizacion(unittest.TestCase):
    def test_calcular_costo_total(self):
        aluminio_pulido = Aluminio("Pulido", 50700)
        vidrio_transparente = Vidrio("Transparente", 8.25)
        ventana1 = Ventana("O", 120, 90, aluminio_pulido, vidrio_transparente, 1)
        ventana2 = Ventana("X", 100, 80, aluminio_pulido, vidrio_transparente, 2)

        cliente = Cliente("Juan Perez", "Constructora XYZ")
        cotizacion = Cotizacion(cliente, [ventana1, ventana2])

        costo_total_esperado = ventana1.calcular_costo_ventana() + ventana2.calcular_costo_ventana()
        self.assertEqual(cotizacion.calcular_costo_total(), costo_total_esperado)

if __name__ == '__main__':
    unittest.main()
