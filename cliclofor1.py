#crear cicle for que permita ingresar 10 numeros. Mostrar cuantos son numeros pares y cuantos son impares
par=0
impar=0
for 1 in range(10):
    nume=int(input("Digite un numer: "))
    if(nume%2==0:
        par=par+1)
    else:
        impar=impar+1
print("La cantidad de numeros pares es: "+ str(par))
print("La cantidad de numeros impares es: "+ str(impar))