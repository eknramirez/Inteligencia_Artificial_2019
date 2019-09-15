# Ejercicio para Inteligencia Artificial, Por medio del cual se
# Crea una Calculadora de Bases Numericas.
def Bin_A_Decimal():
    numero_Binario=input("Ingrese Aqui su Numero Binario: ")
    Aux_binario=numero_Binario
    Lista_Num = numero_Binario[::-1]
    Salida = 0; Exponente =0;

    while  Exponente < len(Lista_Num):
        if int(Lista_Num[Exponente])== 1:
            Salida += int(Lista_Num[Exponente]) * 2 ** Exponente
        Exponente += 1
    print("El Numero ingresado es:",numero_Binario)
    print("El resultado de la conversion es :",Salida)

    f = open('resultados.txt', 'a')
    f.write("El numero: " + str(Aux_binario) + " A n umero Decimal es : " + str(Salida) + "\n")
    f.close()


def Menu():
    print("CALCULADORA DE BASES NUMERICAS:\n")
    print("Elige una Opcion Correspondiente.")
    print("Opcion 1. Convertir A Binarios: ")
    print("Opcion 2. Convertir a Bases Numericas.")
    print("Opcion 3. Convertir a Decimal. ")
    print("Opcion 4. Convertir Decimal a Hexadecimal")

def DecimalAHexodecimal(): # Esta sera nuestra función principal
    decimal = int(input("Introduzca un numero positivo para convertirlo a hexodecimal: ")) # Pedimos los decimales al usuario
    hexadecimal = "" # En esta variable almacenaremos el valor hexodecimal
    Aux_Decimal=decimal
    while decimal != 0:
        # Cambiamos los digitos por los hexodecimales
        rem = CambiarDigitos(decimal % 16)
        # Llenamos la varibale "hexodecimal" con los nuevos valores
        hexadecimal = str(rem) + hexadecimal
        decimal = int(decimal / 16)

    print("Resultado: " + hexadecimal) # Mostramos el resultado
    f = open('resultados.txt', 'a')
    f.write("El numero Decimal : "+str(Aux_Decimal)+" Es igual a el Hexadecimal: "+str(hexadecimal)+"\n")
    f.close()
def CambiarDigitos(digitos): # Esta funcion traduce los digitos a sus respectivos hexodecimales
    decimales =     [10 , 11 , 12 , 13 , 14 , 15 ]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for c in range(7):
        if digitos == decimales[c - 1]:
            digitos = hexadecimal[c - 1]
    return digitos

Menu()
opcion=int(input("Ingrese su Opcion:"))

if(opcion==1 ):
    def binarizar(decimal):
        binario = ''
        while decimal // 2 != 0:
            binario = str(decimal % 2) + binario
            decimal = decimal // 2
        return str(decimal) + binario
    numero = int(input('Introduce el número a convertir a binario: '))
    aux_numero_bin=numero
    print("El numero Binario es:",binarizar(numero))
    print("Resultado: " + binarizar(numero))  # Mostramos el resultado
    f = open('resultados.txt', 'a')
    f.write("El numero Binarioi : " + str(aux_numero_bin) + " Es igual a Decimal: " + str(binarizar(numero)) + "\n")
    f.close()
elif(opcion==2):
    # Ingresar un numero  entero para cambiarlo a la base correspondiente.
    def cambio_base(decimal, base):
        conversion = ''
        while decimal // base != 0:
            conversion = str(decimal % base) + conversion
            decimal = decimal // base
        return str(decimal) + conversion
    numero = int(input('Introduce el número a cambiar de base: '))
    aux_numero =numero
    base = int(input('Introduce la base: '))
    print("La conversion o Resultado es: ")
    pass
    print(cambio_base(numero, base))


    f = open('resultados.txt', 'a')
    f.write("El numero: " + str(aux_numero) + "En base : "+str(base)+"  Es igual a: "+ str(cambio_base(numero,base)) + "\n")
    f.close()


elif(opcion==3):
    print("Ingresaste  a Conversion de Binario a Decimal.")
    Bin_A_Decimal()

elif(opcion==4):
    DecimalAHexodecimal()


