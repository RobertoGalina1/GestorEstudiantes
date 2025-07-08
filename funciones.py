from random import randint,seed

def hash_propia(nombre):
    seed(nombre)
    cantidad = len(nombre)
    caracteres = [str(x) for x in range(1,cantidad*randint(3,10))]
    #print(caracteres)
    id = "".join(caracteres[-1:-9:-2])
    #print(id)
    return int(id)
    
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
    estudiante_id  = hash_propia(nombre.lower())
    estudiante[estudiante_id] = {'nombre':nombre,
                                 'edad': edad,
                                 'materias del semestre':materias_tuplas,
                                 'calificaciones':calificaciones}
    return estudiante    

def mostrar_resumen(diccionario):
    if not diccionario:
        print("¡No se han registrado estudiantes!")
        return
    print("--------------------ESTUDIANTES REGISTRADOS--------------------")
    
    for id,info in diccionario.items():
        print(20*"-")
        print("ID del estudiante: ",id)
        print("Nombre: ",info['nombre'])
        print("Edad: ",info['edad'])
        print('Materias y Calificaciones')
        print(20*"-")
        for materia,cali in info['calificaciones'].items():
            print(f'|{materia} --- {cali}|')
        promedio = sum(info['calificaciones'].values())/len(info["calificaciones"])
        print('Promedio: ',promedio)
        print(20*"-")
        

def mostrar_aprobados(diccionario):
    aprobados = False
    for id,info in diccionario.items():
        promedio = sum(info['calificaciones'].values())/len(info["calificaciones"])
        if promedio >= 6:
            aprobados = True
            print(20*"-")   
            print("ID del estudiante: ",id)
            print("Nombre: ",info['nombre'])
            print("Edad: ",info['edad'])
            print('Materias y Calificaciones')
            print(20*"-")
            print({materia:(cali,'aprobado') if cali >=  6 else (cali,'reprobado') for materia,cali in info['calificaciones'].items()})
            print('Promedio',promedio)
            print(20*"-")
    if not aprobados:
        print("Ningún alumno tiene el promedio aprobatorio")

def buscar_por_id(diccionario,id):
    return diccionario.get(id,"Alumno no presente")


            

hash_propia("Ruben")
hash_propia("Arturo Carlos")
hash_propia("Armando Perez de la sal")
hash_propia("Adela")
print(hash_propia("roberto"))

