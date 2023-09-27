"""

#Entrada: Numero. Salida: True si es positivo
numero=int(input("numero: "))
print ("Es postivo? ")
esPositivo=(numero>0)
if esPositivo:
  print("es positivo")
elif numero == 0:
  print("Es 0")
else:
    print("Es negativo")
"""

#Entrada numero. Salida true si esta aprobado
nota=int(input("nota: "))
print ("Esta aprobado? ")
if nota<0 or nota>10:
    print ("la nota no es valida")
elif nota>=0 and nota<5:
    print("Esta suspenso")
elif nota==5:
    print("aprobado por los pelos")
elif nota<7:
    print("tienes un bien")
elif nota<9:
    print ("tienes un notable")
else:
    print("sobresaliente")
"""
nota =int(input("nota: "))
print ("esta aprobado?")
if nota<0 or nota>10:
    print ("la nota no es valida")
elif nota>=9:
    print("sobresaliente")
elif nota>=7:
    print("notable")
elif nota>=6:
    print("bien")
elif nota>=5:
    print("sufieciente")
else:
    print("suspenso")
"""
            # Debieramos usar las opciones mas usadas al principio, si vamos a tener mas sobresalientes es mas eficiente empezar desde al 10 hasta el 0
