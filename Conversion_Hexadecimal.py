def DecimalAHexodecimal(): # Esta sera nuestra función principal
    decimal = int(input("Introduzca un numero positivo para convertirlo a hexodecimal: ")) # Pedimos los decimales al usuario
    hexadecimal = "" # En esta variable almacenaremos el valor hexodecimal
    while decimal != 0:
        # Cambiamos los digitos por los hexodecimales
        rem = CambiarDigitos(decimal % 16)
        # Llenamos la varibale "hexodecimal" con los nuevos valores
        hexadecimal = str(rem) + hexadecimal
        decimal = int(decimal / 16)
    print("Resultado: " + hexadecimal) # Mostramos el resultado

def CambiarDigitos(digitos): # Esta funcion traduce los digitos a sus respectivos hexodecimales
    decimales =     [10 , 11 , 12 , 13 , 14 , 15 ]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for c in range(7):
        if digitos == decimales[c - 1]:
            digitos = hexadecimal[c - 1]
    return digitos

DecimalAHexodecimal()