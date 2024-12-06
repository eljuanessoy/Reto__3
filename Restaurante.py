class MenuItem:
    def __init__(self, nombre, precio, impuesto, propina):
        self.precio = precio
        self.impuesto = impuesto
        self.propina = propina
        self.nombre = nombre

    def calcularPrecio(self):
        impuesto = self.precio * self.impuesto
        propina = self.precio * self.propina
        total = self.precio + impuesto + propina
        return total
    
class Entrada(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, tipo):
        super().__init__(nombre, precio, impuesto, propina)
        self.tipo = tipo

class Postre(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, tipo):
        super().__init__(nombre, precio, impuesto, propina)
        self.tipo = tipo

class Bebida(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, tipo):
        super().__init__(nombre, precio, impuesto, propina)
        self.tipo = tipo

class Ensalada(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, vinagreta):
        super().__init__(nombre, precio, impuesto, propina)
        self.vinagreta = vinagreta

class Fuerte(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, tipo):
        super().__init__(nombre, precio, impuesto, propina)
        self.tipo = tipo

class Order:
    def __init__(self):
        self.items = []
    
    def agregarItem(self, item):
        self.items.append(item)       

    def calcularTotal(self):
        total = 0
        for item in self.items:
            total += item.calcularPrecio()
        return total

    def imprimirFactura(self):
        for item in self.items:
            print(item.nombre, "- $",item.calcularPrecio())
        print("Total: $",self.calcularTotal())
    
    def aplicarDescuento(self):        
        total = self.calcularTotal()
        if total > 450000:
            for item in self.items:
                item.precio = item.precio * 0.9
  


entrada1 = Entrada("Cacerola de Patatas Bravas", 56800, 0.7, 0.10, "Queso")
entrada2 = Entrada("Ración de Jamón Ibérico de Bellota", 223500, 0.7, 0.10, "Carne")
entrada3 = Entrada("Carpaccio de Salmón", 70000, 0.7, 0.10, "Pescado")

fuerte1 = Fuerte("Spaguetti a la Fiorentina", 44600, 0.7, 0.10, "Spaghetti")
fuerte2 = Fuerte("Pasta Pomodoro", 70000, 0.7, 0.10, "Pasta corta")
fuerte3 = Fuerte("Spaguetti al Guanciale", 75000, 0.7, 0.10, "Spaghetti")
fuerte4 = Fuerte("Pasta a la Rueda con Prosciutto y manzana confitada", 85000, 0.7, 0.10, "Fetuccini")
fuerte5 = Fuerte("Paella Mixta", 149800, 0.7, 0.10, "Paella")

postre1 = Postre('Torta Philadelphia', 29800, 0.7, 0.10, "Tarta")
postre2 = Postre("Copa Amaretto", 26000, 0.7, 0.10, "Copa")
postre3 = Postre("Gelato al Pistacchio", 40000, 0.7, 0.10, "Gelatina")
postre4 = Postre("Afogatto", 26000, 0.7, 0.10, "Helado")

bebida1 = Bebida("Bubble Fizz", 50000, 0.7, 0.10, "Licor")
bebida2 = Bebida("Capuccino", 10000, 0.7, 0.10, "Bebida caliente")
bebida3 = Bebida("Gassata de Frutos Verdes", 18900, 0.7, 0.10, 'Refresco')
bebida4 = Bebida("Limonada de Mango Biche", 16500, 0.7, 0.10, "Limonada")
bebida5 = Bebida("Jugo de Mora", 10000, 0.7, 0.10, "Jugo")

ensalada1 = Ensalada("Insalata Di garedino", 55000, 0.7, 0.10, "Vinagreta Oliva Limón")
ensalada2 = Ensalada("Vero Amore", 51000, 0.7, 0.10, "Vinagreta tradicional")



orden1 = Order()
orden1.agregarItem(ensalada2)
orden1.agregarItem(fuerte3)
orden1.agregarItem(postre3)
orden1.agregarItem(bebida4)

orden2 = Order()
orden2.agregarItem(entrada2)
orden2.agregarItem(fuerte5)
orden2.agregarItem(postre1)
orden2.agregarItem(bebida3)

orden3 = Order()
orden3.agregarItem(entrada1)
orden3.agregarItem(fuerte1)
orden3.agregarItem(postre4)
orden3.agregarItem(bebida3)


orden = int(input("Ingrese una orden, 1, 2, 3: "))

if orden == 1:
    print()
    print("La factura de la orden 1 es:")
    print()
    orden1.aplicarDescuento()
    orden1.imprimirFactura()
    print()

elif orden == 2:
    print()
    print("La factura de la orden 2 es:")
    print()
    orden2.aplicarDescuento()
    orden2.imprimirFactura()
    print()

elif orden == 3:
    print()
    print("La factura de la orden 3 es:")
    print()
    orden3.aplicarDescuento()
    orden3.imprimirFactura()
    print()

else:
    print("Ingrese un método válido")