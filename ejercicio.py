def nombre_del_usuario():
    nombre=input("ingresar el nombre del usuario")
    apellido=input("ingresar el apellido del usuario")
    edad_del_usuario(nombre,apellido)

def edad_del_usuario(nombre,apellido):
    nombre=nombre
    apellido=apellido
    a1=int(input("ingrese año de nacimiento"))
    a2=int(input("ingrese año actual"))
    edad=a2-a1
    if edad >=18:
        print("Mayor de edad")
    else:
        print("Menor de edad")
    informacion(nombre,apellido,edad)

def informacion(nombre,apellido,edad):
    print("El nombre del usuario es "+nombre+" "+apellido+" y tiene "+str(edad)+" años")

nombre_del_usuario()
