import math

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

#Creamos la función para hallar la longitud de la linea (Teorema de pitagoras)

    def compute_length(self):
        return math.sqrt((self.end[0] - self.start[0])**2 + (self.end[1] - self.start[1])**2)

#Creamos la función para hallar la pendiente (pendiente = arctan(co/ca))

    def compute_slope(self):
        if self.end[0] - self.start[0] != 0:
            pendiente = (self.end[1] - self.start[1]) / (self.end[0] - self.start[0])
            return math.degrees(math.atan(pendiente))
        else:
            return None

#Creamos la función para hallar si hay cruce o no en el eje x: (El signo end_y sea diferente al signo de start_y)

    def compute_horizontal_cross(self):
        if self.start[1] < 0 and self.end[1] > 0 or self.start[1] > 0 and self.end[1]<0:
            return True
        else:
            return False
        
#Creamos la función para hallar si hay cruce o no en el eje y (El signo end_x sea distinto al signo de start_x)   

    def compute_vertical_cross(self):
        if (self.start[0] < 0 and self.end[0] > 0) or (self.start[0] > 0 and self.end[0]<0):
            return True
        else:
            return False


x1 = float(input("Ingrese la coordenada x de inicio: "))
y1 = float(input("Ingrese la coordenada y de inicio: "))
x2 = float(input("Ingrese la coordenada x de final: "))
y2 = float(input("Ingrese la coordenada y de final: "))

start = (x1, y1)
end = (x2, y2)
 
line = Line(start, end)
pendiente = line.compute_slope() 
interseccion_eje_y = line.compute_vertical_cross()
interseccion_eje_x = line.compute_horizontal_cross()

print("La longitud de la línea es: ", line.compute_length()) 
print("La pendiente en grados de la línea es: ", line.compute_slope())  

if interseccion_eje_y:
    print("La línea cruza el eje y")
else:
    print("La línea no cruza el eje y")

if interseccion_eje_x:
    print("La línea cruza el eje x")
else:
    print("La línea no cruza el eje x")