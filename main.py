import numpy as np

def crear_array():
    """Crea un array del 1 al 10 y lo reestructura a una matriz de 2x5."""
    array = np.arange(1, 11).reshape(2, 5)
    print(f"Array:\n{array}\nShape: {array.shape}, Size: {array.size}, Dimensions: {array.ndim}\n")
    return array

def operaciones_basicas(array):
    """Realiza operaciones básicas (suma, resta, multiplicación y división) con un array de unos."""
    ones = np.ones(array.shape)
    suma = array + ones
    resta = array - ones
    multiplicacion = array * ones
    division = array / ones
    
    print(f"Operaciones básicas:\nSuma:\n{suma}\nResta:\n{resta}\nMultiplicación:\n{multiplicacion}\nDivisión:\n{division}\n")

def suma_elementos(array):
    """Calcula la suma de todos los elementos del array."""
    suma_total = np.sum(array)
    print(f"Suma de todos los elementos: {suma_total}\n")

def estadisticas_aleatorias(size=10):
    """Genera un array aleatorio y calcula media, desviación estándar y varianza."""
    random_array = np.random.rand(size)
    media = np.mean(random_array)
    desviacion = np.std(random_array)
    varianza = np.var(random_array)

    print(f"Estadísticas sobre array aleatorio:\nArray: {random_array}\nMedia: {media}\nDesviación estándar: {desviacion}\nVarianza: {varianza}\n")

    # Muestra las listas generadas por slicing progresivo
    slices = [random_array[i:] for i in range(size)]
    print(f"Slices progresivos del array:\n{slices}\n")

    # Suma 10 al array y calcula estadísticas nuevamente
    desplazado = random_array + 10
    print(f"Estadísticas tras sumar 10:\nMedia: {np.mean(desplazado)}, Desviación estándar: {np.std(desplazado)}, Varianza: {np.var(desplazado)}\n")

    # Raíz cuadrada de los elementos desplazados
    print(f"Raíz cuadrada del array desplazado:\n{np.sqrt(desplazado)}\n")

def producto_punto():
    """Genera un array aleatorio 3x2 y calcula el producto punto con su transpuesta."""
    matriz = np.random.rand(3, 2)
    producto = np.dot(matriz, matriz.T)
    print(f"Matriz original:\n{matriz}\n\nProducto punto con su transpuesta:\n{producto}\n")

def guardar_cargar_array(array, filename="array.npy"):
    """Guarda un array en un archivo .npy y lo carga para verificar."""
    np.save(filename, array)
    cargado = np.load(filename)
    print(f"Array guardado y cargado correctamente:\n{cargado}\n")

def main():
    """Función principal que orquesta la ejecución de todas las funciones."""
    array = crear_array()
    operaciones_basicas(array)
    suma_elementos(array)
    estadisticas_aleatorias()
    producto_punto()
    guardar_cargar_array(array)

if __name__ == "__main__":
    main()