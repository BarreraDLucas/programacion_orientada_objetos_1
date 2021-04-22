
def funciones():
    cont = 0
    acum1 = 0
    cant_sin = 0
    cont_fcon = 0
    cant_espec = int(input("Ingrese la cantidad de espectadores: "))
    while cant_espec != 0:
        cant_desc = int(input("Ingrese la cantidad de espectadores con descuento: "))
        if cant_desc != 0:
            cont_fcon = cont_fcon + 1
        acum1 = acum1 + cant_desc
        cant_sin = (cant_espec-acum1)
        cont = cont+1
        cant_espec = int(input("Ingrese la cantidad de espectadores: "))

    porcentaje_descuento = 100 * cont_fcon / cont
    recaudacion_total = (acum1 * 50)+(cant_sin * 75)
    print(f"La recaudación total del cine es de: {recaudacion_total}")
    print(f"El porcentaje de funciones con descuento es de: {porcentaje_descuento}%")


funciones()
