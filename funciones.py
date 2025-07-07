def registrar_estudiante():
    estudiante = {}
    calificaciones = {}
    nombre = input("Ingrese el nombre completo del estudiante:")
    edad = input("Ingresar la edad del estudiante:")
    materias = input("Ingrese las materias de inscritas en el semestre (separado por comas):").split(',')
    materias_tuplas = tuple(materias)
    for materia in materias_tuplas:
        print("Materia: ",materia)
        calificacion = float(input('Ingrese la calificación:'))
        calificaciones[materia.lower()] = calificacion
    estudiante_hash = list(str(int(hash(nombre))))
    estudiante_id = "".join(estudiante_hash[1::2])
    estudiante[estudiante_id] = {'nombre':nombre,
                                 'edad': edad,
                                 'materias del semestre':materias_tuplas,
                                 'calificaciones':calificaciones}
    print(estudiante)
    return estudiante    

registrar_estudiante()