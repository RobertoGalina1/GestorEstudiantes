def registrar_estudiante():
    estudiante = {}
    calificaciones = {}
    nombre = input("Ingrese el nombre completo del estudiante:")
    edad = int(input("Ingresar la edad del estudiante:"))
    materias = input("Ingrese las materias de inscritas en el semestre (separado por comas):").split(',')
    materias_tuplas = tuple(materias)
    for materia in materias_tuplas:
        print("Materia:",materia)
        calificacion = float(input('Ingrese la calificación:'))
        calificaciones[materia] = calificacion
    estudiante_hash = list(str(int(hash(nombre))))
    estudiante_id = "".join(estudiante_hash[1::2])
    estudiante[estudiante_id] = {'nombre':nombre,
                                 'edad': edad,
                                 'materias del semestre':materias_tuplas,
                                 'calificaciones':calificaciones}
    return estudiante    

def mostrar_resumen(diccionario):
    if not diccionario:
        print("¡No se han registrado estudiantes!")
        return
    print("ESTUDIANTES REGISTRADOS")
    for id,info in diccionario.items():
        print("ID del estudiante: ",id)
        print("Nombre: ",info['nombre'])
        print("Edad: ",info['edad'])
        print('Materias y Calificaciones')
        print("*****************************************")
        for materia,cali in info['calificaciones'].items():
            print(materia," --- ",cali)
        print("Promedio: ",sum(info['calificaciones'].values())/len(info['calificaciones']))
        print("*****************************************")





