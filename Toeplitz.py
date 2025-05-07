import scipy
from scipy.linalg import toeplitz

# Definir los vectores con valores fijos
x = [1, 2, 3, 4]  # x(n) con valores fijos
h = [1,0,0,0]     # h(n) con valores fijos

# Mostrar los vectores definidos
print("x(n) definido:", x)
print(f"Tamaño de N1: {len(x)} elementos\n")

print("h(n) definido:", h)
print(f"Tamaño de N2: {len(h)} elementos\n")

N = len(x) + len(h) - 1

print(N, "= N1 + N2 - 1\n") 

# Función para Zero-Padding
xpadding = x + [0] * (N - len(x))
hpadding = h + [0] * (N - len(h))

print("x zero padding definido:", xpadding)
print("h zero padding definido:", hpadding)


# Definir la función para calcular y
def calcular_y(H, x, N):
    y = []
    for i in range(N):  # Iterar sobre las filas de H
        suma = 0
        for j in range(N):  # Iterar sobre las columnas de H
            suma += H[i][j] * x[j]  # Producto y acumulación
        y.append(int(suma))  # Convertir la suma a entero
    return y

# Preparar columna y fila para matriz circulante
c = hpadding
r = [hpadding[0]] + hpadding[:0:-1]  # reversa menos el primero

def construir_toeplitz(c, r):
    # Crear matriz Toeplitz usando scipy
    H_array = toeplitz(c, r)
    # Convertir a listas de enteros estándar
    H = [list(map(int, row)) for row in H_array]
    return H

# Construir matriz Toeplitz normal
H = construir_toeplitz(c, r)

# Mostrar matriz Toeplitz normal
print("Matriz Toeplitz:")
for row in H:
    print(row)

# Matriz traspuesta de Toeplitz
def transpuesta(H):
    filas = len(H)
    columnas = len(H[0])
    T = [[0 for _ in range(filas)] for _ in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            T[j][i] = H[i][j]
    return T

T = transpuesta(H)
print("\nTraspuesta Matriz Toeplitz:")
for row in T:
    print(row)

# Llamar a la función para calcular y usando la transpuesta y xpadding
y = calcular_y(T, xpadding, N)

# Resultado final
print("\ny(n):", y)
print(f"Tamaño de y(n): {len(y)} elementos\n")

