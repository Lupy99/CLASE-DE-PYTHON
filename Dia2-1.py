"""
print("introduce tu nombre: ")      #el input recoge el dato y lo guarda en nombre
nombre = input()
print ("hola " + nombre)

nombre = input("instroduce tu nombre: ")
print ("hola "+ nombre)
#Existen dos tipos de =s en proramacion:
#   =   -> Asigna lo que hay a la izquierda a lo que hay a la derecha.EJ: numero=5
#   ==  -> Es un igual LOGICO. Compara los valores que tiene a izquierda y derecha. Devuelve true(iguales) o false(distintas)

#1.-Entrada un numero. Salida=True si es mayor de edad
  print ("introduce un numero: ")
  edad=input()
  print=("es mayor de edad?")
  print (str(edad>=18))

# Cuando hacemos un input el valor siempre lo guarda como str. Si queremos que sea un int hay que transformarlo
edad = int(input("edad: "))
print ("es mayor de edad?")
#print (edad>=18)
if (edad>=18):
    print("si, es mayor de edad")
else:
    print("no es mayor de edad")

edad = (int(input("introduce tu edad: "))
        print("es mayor de edad?")
        print(esMayorEdad)
print(type(esMayorEdad))
if es MayorEdad:
  print("Es mayor de edad")
else
  print ("Es menor de edad")
print ("se imprime siempre")
"""
#Entrada: Numero. Salida: True si es positivo
numero=int(input("numero: "))
print ("Es postivo? "+str(numero>=0))
print (numero>=0)
esPositivo=(numero>=0)
if esPositivo:
  print("es positivo")
else:
  print("es negativo")


#Entrada numero. Salida true si esta aprobado
nota=int(input("nota: "))
print ("esta aprobado? "+ str(nota>=5 and nota<=10))
print (nota>=5 and nota<=10)



#Entrada dia de la semana. Salida true si findesemana
print ("introduce un dia de la semana: ")
dia= input()
print("es fin de semana? :" + str(dia=="sabado" or dia=="domingo"))

#Entrada una letra. Salida true si es vocal
#print ("introduce una letra: ")
letra=input("introduce una letra: ")
print ("es vocal? " + str(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u"))
