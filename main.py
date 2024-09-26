from app.clases import Aluminio, Vidrio, Ventana, Cliente, Cotizacion

def main():
    # Crear tipos de aluminio
    aluminio_pulido = Aluminio("Pulido", 50700)
    aluminio_lacado_bril = Aluminio("Lacado Brillante", 54200)

    # Crear tipos de vidrio
    vidrio_transparente = Vidrio("Transparente", 8.25)
    vidrio_bronce = Vidrio("Bronce", 9.15, esmerilado=True)

    # Crear ventanas
    ventana1 = Ventana("O", 120, 90, aluminio_pulido, vidrio_transparente, 1)
    ventana2 = Ventana("XO", 180, 90, aluminio_lacado_bril, vidrio_bronce, 2)

    # Crear cliente
    cliente = Cliente("Constructora ABC", "Empresa XYZ")

    # Crear cotización
    cotizacion = Cotizacion(cliente, [ventana1, ventana2])

    # Calcular y mostrar el costo total
    costo_total = cotizacion.calcular_costo_total()
    print(f"El costo total de la cotización es: ${costo_total:.2f}")

if __name__ == "__main__":
    main()
