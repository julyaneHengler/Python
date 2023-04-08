valor1 = int(input('Digite valor 1: '))
valor2 = int(input('Digite valor 2: '))
valor3 = int(input('Digite valor 3: '))
if (valor1 < valor2) and (valor2 < valor3):
    print (valor1, valor2, valor3)
elif (valor1 < valor3) and (valor3 < valor2):
    print (valor1, valor3, valor2)
elif (valor2 < valor1) and (valor1 < valor3):
    print (valor2, valor1, valor2)
elif (valor2 < valor3) and (valor3 < valor1):
    print (valor2, valor3, valor2)
elif (valor3 < valor1) and (valor1 < valor2):
    print (valor3, valor1, valor2)
else:
    print ("Os valores são:", valor3, valor2, valor1)
