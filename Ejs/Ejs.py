#Producto cartesiano de dos listas
colores = ["rojo", "verde"]
tallas = ["S", "M", "L"]
combinaciones = [(color, talla) for color in colores for talla in tallas]
print(combinaciones)

#Matriz 3x3 con ceros excepto en la diagonal
matriz_identidad = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print(matriz_identidad)

#uso de map para aplicar una funcion lambda a cada elemento de una lista
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

#uso de filter con lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

#uso de sorted con lambda para ordenar con una clave personalizada
personas = [
    {"nombre": "Hanan", "edad": 25},
    {"nombre": "Eddy", "edad": 4},
    {"nombre": "Ángel", "edad": 25}
]

ordenadas = sorted(personas, key = lambda p: p["edad"])
print(ordenadas)