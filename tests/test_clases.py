import unittest
from app.clases import Aluminio, Vidrio, Ventana, Cotizacion, Cliente

class TestClases(unittest.TestCase):
    def setUp(self):
        # Crear objetos para las pruebas
        self.aluminio = Aluminio('Pulido', 50700)
        self.vidrio = Vidrio('Transparente', 8.25)
        self.ventana = Ventana('O', 120, 90, self.aluminio, self.vidrio, esmerilado=False)

    def test_calculo_aluminio(self):
        metros_lineales = self.ventana.calcular_metros_lineales()
        costo_aluminio = self.aluminio.calcular_costo(metros_lineales)
        self.assertEqual(round(costo_aluminio), 15210)

    def test_calculo_vidrio(self):
        area_cm2 = self.ventana.calcular_area_ventana()
        costo_vidrio = self.vidrio.calcular_costo(area_cm2 / 100, esmerilado=False)
        self.assertEqual(round(costo_vidrio), 891)

    def test_calculo_ventana(self):
        costo_total = self.ventana.calcular_costo()
        self.assertEqual(round(costo_total), 16101)

if __name__ == '__main__':
    unittest.main()
