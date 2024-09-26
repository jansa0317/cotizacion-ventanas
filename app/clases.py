class Aluminio:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio  # Atributo corregido

class Vidrio:
    def __init__(self, nombre, precio, esmerilado=False):
        self.nombre = nombre
        self.precio = precio  # Atributo corregido
        self.esmerilado = esmerilado

class Ventana:
    def __init__(self, estilo, ancho, alto, aluminio, vidrio, num_naves):
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.aluminio = aluminio
        self.vidrio = vidrio
        self.num_naves = num_naves

    def calcular_costo_ventana(self):
        # Cálculo del perímetro de aluminio (considera esquinas)
        perimetro = (2 * self.ancho) + (2 * self.alto) - (8 * self.num_naves)
        costo_aluminio = perimetro * self.aluminio.precio

        # Cálculo del área de vidrio
        area_ventana = (self.ancho - 1.5) * (self.alto - 1.5)
        costo_vidrio = area_ventana * self.vidrio.precio

        # Si el vidrio es esmerilado, agregar el costo adicional
        if self.vidrio.esmerilado:
            costo_vidrio += area_ventana * 5.20  # Precio adicional del esmerilado

        # Cálculo de costo de esquinas y chapas
        costo_esquinas = 4 * 4310  # 4 esquinas por ventana
        costo_chapas = 16200 if "X" in self.estilo else 0  # Costo de la chapa si hay una nave X

        return costo_aluminio + costo_vidrio + costo_esquinas + costo_chapas

class Cliente:
    def __init__(self, nombre, empresa):
        self.nombre = nombre
        self.empresa = empresa

class Cotizacion:
    def __init__(self, cliente, ventanas):
        self.cliente = cliente
        self.ventanas = ventanas

    def calcular_costo_total(self):
        costo_total = sum(ventana.calcular_costo_ventana() for ventana in self.ventanas)
        # Aplicar descuento si hay más de 100 ventanas
        if len(self.ventanas) > 100:
            costo_total *= 0.9  # 10% de descuento
        return costo_total
