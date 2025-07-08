from funciones import *

estudiantes = {}

print("Gestor estudiantil".upper())
print("Bienvenido a  la base de datos de la escuela. Que requiere hacer")
menu()
resp = input('Ingrese la operación a realizar: ')
while resp != '0':
    if resp == '1':
        estudiantes.update(registrar_estudiante())
    elif resp == '2':
        mostrar_resumen(estudiantes)
    elif resp == '3':
        mostrar_aprobados(estudiantes)
    elif resp == '4':
        id_buscado = int(input("Ingrese el ID del estudiante buscado: "))
        estudiante_buscado = buscar_por_id(estudiantes,id_buscado)
        print(estudiante_buscado)
    elif resp == '5':
        menu()
    else:
        print("Opción no disponible")
    resp = input('Ingrese la operación a realizar: ')