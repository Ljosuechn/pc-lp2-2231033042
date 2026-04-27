class Pasajero:

    RUTAS_VALIDAS = [
        "Iquitos-Nauta",
        "Iquitos-Yurimaguas",
        "Iquitos-Pucallpa",
        "Iquitos-Sta. Rosa"
    ]

    PESO_LIBRE = 15.0
    PESO_MAXIMO = 25.0

    def __init__(self, dni, nombre_completo, edad, peso_equipaje, ruta):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.peso_equipaje = peso_equipaje
        self.ruta = ruta

    # PROPERTY: DNI
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, valor):
        if not isinstance(valor, str) or len(valor) != 8 or not valor.isdigit():
            raise ValueError("El DNI debe ser una cadena de exactamente 8 dígitos numéricos.")
        self.__dni = valor

    # PROPERTY: NOMBRE COMPLETO
    @property
    def nombre_completo(self):
        return self.__nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena válida.")
        valor = valor.strip().title()
        if len(valor) < 5:
            raise ValueError("El nombre completo debe tener al menos 5 caracteres.")
        self.__nombre_completo = valor

    # PROPERTY: EDAD
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, int):
            raise ValueError("La edad debe ser un número entero.")
        if not (0 <= valor <= 120):
            raise ValueError("La edad debe estar entre 0 y 120 años.")
        self.__edad = valor

    # PROPERTY: PESO EQUIPAJE
    @property
    def peso_equipaje(self):
        return self.__peso_equipaje

    @peso_equipaje.setter
    def peso_equipaje(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("El peso del equipaje debe ser un número.")
        if not (0 <= valor <= self.PESO_MAXIMO):
            raise ValueError(f"El peso del equipaje debe estar entre 0 y {self.PESO_MAXIMO} kg.")
        self.__peso_equipaje = float(valor)

    # PROPERTY: RUTA
    @property
    def ruta(self):
        return self.__ruta

    @ruta.setter
    def ruta(self, valor):
        if valor not in self.RUTAS_VALIDAS:
            raise ValueError(f"Ruta inválida. Rutas permitidas: {self.RUTAS_VALIDAS}")
        self.__ruta = valor

    # PROPERTY CALCULADA: CATEGORÍA DE EDAD
    @property
    def categoria_edad(self):
        if self.edad < 12:
            return "Niño"
        elif self.edad <= 17:
            return "Adolescente"
        elif self.edad <= 59:
            return "Adulto"
        else:
            return "Adulto mayor"

    # PROPERTY CALCULADA: TARIFA BASE
    @property
    def tarifa_base(self):
        if self.ruta == "Iquitos-Nauta":
            return 25
        elif self.ruta == "Iquitos-Sta. Rosa":
            return 80
        elif self.ruta == "Iquitos-Yurimaguas":
            return 120
        elif self.ruta == "Iquitos-Pucallpa":
            return 180

    # PROPERTY CALCULADA: RECARGO EQUIPAJE
    @property
    def recargo_equipaje(self):
        exceso = self.peso_equipaje - self.PESO_LIBRE
        if exceso > 0:
            return exceso * 2
        return 0

    # PROPERTY CALCULADA: TARIFA TOTAL
    @property
    def tarifa_total(self):
        base = self.tarifa_base
        recargo = self.recargo_equipaje

        if self.categoria_edad in ["Niño", "Adulto mayor"]:
            base *= 0.5  # descuento del 50%

        return base + recargo

    # REPRESENTACIÓN EN TEXTO
    def __str__(self):
        return (
            "=== BOLETA DE EMBARQUE ===\n"
            f"DNI: {self.dni}\n"
            f"Nombre: {self.nombre_completo}\n"
            f"Edad: {self.edad} ({self.categoria_edad})\n"
            f"Ruta: {self.ruta}\n"
            f"Peso equipaje: {self.peso_equipaje} kg\n"
            f"Tarifa base: S/. {self.tarifa_base:.2f}\n"
            f"Recargo equipaje: S/. {self.recargo_equipaje:.2f}\n"
            f"TOTAL A PAGAR: S/. {self.tarifa_total:.2f}\n"
        )


# BLOQUE INTERACTIVO
if __name__ == "__main__":
    print("=== REGISTRO DE PASAJERO ===")

    dni = input("Ingrese DNI (8 dígitos): ")
    nombre = input("Ingrese nombre completo: ")
    edad = int(input("Ingrese edad: "))
    peso = float(input("Ingrese peso de equipaje (kg): "))

    print("\nRutas disponibles:")
    print("1. Iquitos-Nauta")
    print("2. Iquitos-Yurimaguas")
    print("3. Iquitos-Pucallpa")
    print("4. Iquitos-Sta. Rosa")

    opcion = input("Seleccione ruta (1-4): ")

    rutas = {
        "1": "Iquitos-Nauta",
        "2": "Iquitos-Yurimaguas",
        "3": "Iquitos-Pucallpa",
        "4": "Iquitos-Sta. Rosa"
    }

    ruta = rutas.get(opcion)

    if ruta is None:
        raise ValueError("Opción de ruta inválida.")

    p = Pasajero(dni, nombre, edad, peso, ruta)

    print("\n=== BOLETA GENERADA ===")
    print(p)

