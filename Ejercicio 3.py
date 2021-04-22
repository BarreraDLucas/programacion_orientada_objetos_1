def menu():
    opcion = int(input("Elija una de las opciones escribiendo 1/2/3/4: "))
    if opcion == 1:
        numero_ingreso = int(input("Ingrese un numero positivo o 0 para finalizar: "))
        acum = 0
        while numero_ingreso != 0 and numero_ingreso > 0:
            acum = acum + (numero_ingreso**2)
            numero_ingreso = int(input("Ingrese un numero positivo o 0 para finalizar: "))
            if numero_ingreso < 0:
                while numero_ingreso < 0:
                    numero_ingreso = int(input("Ingrese un numero válido o 0 para finalizar: "))
        print(f"La suma de los cuadrados de los números ingresados es: {acum}")
    elif opcion == 2:
        texto = input("Ingrese un texto finalizado por punto para saber la cantidad de palabras que finalizan vocal: ")
        contador = 0
        caracter_anterior = ""
        vocales = "aeiouAEIOU"
        for caracter in texto:
            if caracter == " " or caracter == ".":
                if caracter_anterior in vocales:
                    contador += 1
            caracter_anterior = caracter
        print(f"La cantidad de palabras que terminan en vocal es: {contador}")
    elif opcion == 3:
        numero_ingresado = int(input('Ingrese un número para cargar, la carga finaliza con cero: '))
        cont_par = 0
        cont_impar = 0
        while numero_ingresado != 0:
            resto = (numero_ingresado % 2)
            if resto == 0:
                cont_par = cont_par+1
            elif resto != 0:
                cont_impar = cont_impar+1
            numero_ingresado = int(input('Ingrese un número para cargar, la carga finaliza con cero: '))
        if cont_impar > cont_par:
            print("Hay mayor cantidad de números impares")
        elif cont_par > cont_impar:
            print("Hay mayor cantidad de números pares")
        else:
            print("La cantidad de impares y de pares es igual")
    elif opcion == 4:
        print("Programa finalizado")


menu()
