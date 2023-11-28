alumnos = {}

while True:
    print("\nMenú:")
    print("1. Añadir alumno/a")
    print("2. Número de aprobados")
    print("3. Mostrar todo el alumnado")

    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del alumno/a: ")
        aprobado = input("¿Aprobado? (Sí/No): ").lower() == 'si'
        alumnos[nombre] = aprobado
        print(f"{nombre} ha sido añadido/a a la base de datos.")

    elif opcion == '2':
        aprobados = sum(aprobado for aprobado in alumnos.values())
        print(f"El número de aprobados es: {aprobados}")

    elif opcion == '3':
        print("\nAlumnado:")
        for nombre, aprobado in alumnos.items():
            estado = "Aprobado" if aprobado else "Suspendido"
            print(f"{nombre}: {estado}")

    else:
        print("Opción no válida. Intente de nuevo.")
