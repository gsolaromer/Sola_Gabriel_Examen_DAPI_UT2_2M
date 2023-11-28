def ListaNombres(nombres):
    '''Esta función recibe una lista de nombres y la ordena por apellidos en orden alfabético.
Parámetros: Lista de nombres: esta lista de nombres guarda una cantidad indeterminada de nombres en este formato:
['Nombre Apellido 1','Nombre Apellido 2',...,'Nombre Apellido N]
Salida: La función retorna la lista de nombres ordenados alfabéticamente en este formato:
['Apellido, Nombre 1','Apellido, Nombre 2',..,'Apellido, Nombre N]'''
    nombres_ordenados = sorted(nombres, key=lambda x: x.split()[1])
    nombres_formateados = [OrdenarNombre(nombre) for nombre in nombres_ordenados]
    return nombres_formateados

def OrdenarNombre(nombre):
    '''Esta función recibe un 'nombre y apellido' y devuelve el 'apellido, nombre'
Parámetros: Nombre en el formato 'Nombre Apellido'
Salida: Nombre en el formato 'Apellido, Nombre' '''
    partes_nombre = nombre.split()
    apellido = partes_nombre[-1]
    nombre = ' '.join(partes_nombre[:-1])
    nombre_ordenado = f'{apellido}, {nombre}'
    return nombre_ordenado

lista_nombres = ['Juan Perez', 'Maria Lopez', 'Carlos Gomez', 'Ana Rodriguez']
nombres_ordenados = ListaNombres(lista_nombres)
print(nombres_ordenados)