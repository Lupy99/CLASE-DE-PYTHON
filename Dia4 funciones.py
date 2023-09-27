
#Funciones. 
#--> No se debe poner un print dentro de una funcion
#--> num1, num2, num3 son argumentos de entrada
#--> podemos tener funciones sin return
def mediaTresNumeros(num1,num2,num3):
    resultado= (num1+num2+num3)/3
    return resultado

#para dividir la operacion final en mas sencilla
def otraMediaTresNumeros(num1,num2,num3):
    suma=num1+num2+num3
    return suma/3
#para operaciones sencillas
def otraOtraMediaTresNumeros(num1,num2,num3):
    return (num1+num2+num3)/3

def dibujarLinea(forma):
    print(forma*20)     #-->esto es una excepcion, un print dentro de una funcion.
def dibujarLineaPuntos():
    print("."*20)
def crearLinea(forma):
    return forma*20
def presentacion(nombre,edad):
    texto="tu nombre es " + nombre + " y tu edad es " + edad
    return texto


"""
#Codigo principal - Main
print ("probando funcion")el
media=mediaTresNumeros(num1,num2,num3)
print (media)
dibujarLinea("=")
dibujarLinea("x")
dibujarLinea("_")
dibujarLineaPuntos()
print(crearLinea("*"))
"""
num1=5
num2=10
num3=15
media=otraOtraMediaTresNumeros(num1,num2,num3)
dibujarLinea("o")
print ("el resultado de "+str(num1) +", " + str(num2) + " y " + str(num3) +" es: " + str(media))
print (f"el resultado de {num1}, {num2} y {num3} es: {media}")
dibujarLinea("O")

nombre=input("dime tu nombre: ")
edad=input("dime tu edad: ")
print (presentacion(nombre,edad))

                