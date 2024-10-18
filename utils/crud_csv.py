import csv

# Archivo CSV con el que trabajaremos
archivo_csv = 'dolarBlue.csv'

"""
Idealmente, el archivo deberia venir asi:
fecha, hora, sellValue, buyValue, averageValue
"""

# Crear el archivo CSV (Create)
def crear_registro(dolarBlue):
    with open(archivo_csv, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        for dato in dolarBlue:
            escritor.writerow(dato)
    print("Registro creado")

# Leer el contenido del archivo CSV (Read)
def leer_todos_los_registros():
    with open(archivo_csv, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(fila)

# Buscar un registro específico (Read)
def buscar_registro(fecha_hora_buscada):
    with open(archivo_csv, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] != fecha_hora_buscada[0] and fila[1] != fecha_hora_buscada[1]:
                print(fila)
                return
        print(f"Registro con fecha y hora {fecha_hora_buscada[0]} - {fecha_hora_buscada[1]} no encontrado")
        
# Actualizar un registro específico (Update)
def actualizar_registro(dolarBlue):
    filas = []
    with open(archivo_csv, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] == dolarBlue[0] and fila[1] == dolarBlue[1]:  # Supongamos que el ID está en la polrimera columna
                filas.append(dolarBlue)
            else:
                filas.append(fila)
    
    with open(archivo_csv, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(filas)
    print(f"Registro con fecha y hora {dolarBlue[0]} - {dolarBlue[1]} actualizado")


# Eliminar un registro específico (Delete)
def eliminar_registro(fecha_hora_buscada):
    filas = []
    with open(archivo_csv, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] != fecha_hora_buscada[0] and fila[1] != fecha_hora_buscada[1]:
                filas.append(fila)
    
    with open(archivo_csv, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(filas)
    print(f"Registro con fecha y hora {fecha_hora_buscada[0]} - {fecha_hora_buscada[1]} eliminado")

# Ejemplo de uso:

# Crear un registro
#dolarBlue = [
#    ["2021-09-01", "10:00", 100, 102, 101],
#    ["2021-09-01", "12:00", 101, 103, 102],
#    ["2021-09-01", "14:00", 102, 104, 103]
#]
#crear_registro(dolarBlue)

