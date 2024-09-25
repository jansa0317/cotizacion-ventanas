class Aluminio:
    def __init__(self, tipo, precio_por_metro):
        self.tipo = tipo
        self.precio_por_metro = precio_por_metro

    def calcular_costo(self, metros_lineales):
        return self.precio_por_metro * metros_lineales


class Vidrio:
    def __init__(self, tipo, precio_por_cm2, esmerilado_costo_adicional=0):
        self.tipo = tipo
        self.precio_por_cm2 = precio_por_cm2
        self.esmerilado_costo_adicional = esmerilado_costo_adicional

    def calcular_costo(self, area_cm2, esmerilado=False):
        costo_total = self.precio_por_cm2 * area_cm2
        if esmerilado:
            costo_total += self.esmerilado_costo_adicional * area_cm2
        return costo_total


class Ventana:
    def __init__(self, estilo, ancho, alto, aluminio, vidrio, esmerilado=False):
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.aluminio = aluminio
        self.vidrio = vidrio
        self.esmerilado = esmerilado

    def calcular_metros_lineales(self):
        # Calcula el perímetro total de la ventana
        return 2 * (self.ancho + self.alto) / 100  # Convertimos a metros

    def calcular_area_ventana(self):
        # Calcula el área total de la ventana
        return self.ancho * self.alto

    def calcular_costo(self):
        # Costo del aluminio
        metros_lineales = self.calcular_metros_lineales()
        costo_aluminio = self.aluminio.calcular_costo(metros_lineales)

        # Costo del vidrio
        area_cm2 = self.calcular_area_ventana()
        costo_vidrio = self.vidrio.calcular_costo(area_cm2 / 100, self.esmerilado)

        # Costo total
        return costo_aluminio + costo_vidrio


class Cliente:
    def __init__(self, nombre, empresa):
        self.nombre = nombre
        self.empresa = empresa


class Cotizacion:
    def __init__(self, cliente, descuento=0):
        self.cliente = cliente
        self.ventanas = []
        self.descuento = descuento

    def agregar_ventana(self, ventana):
        self.ventanas.append(ventana)

    def calcular_total(self):
        total = sum(ventana.calcular_costo() for ventana in self.ventanas)
        if len(self.ventanas) >= 100:  # Aplicamos descuento si es mayor a 100 ventanas
            total *= (1 - self.descuento / 100)
        return total
