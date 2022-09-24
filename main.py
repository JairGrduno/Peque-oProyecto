def piramideCaracter(cadena, i):
    if (i >= len(cadena)):
        return
    else:
        for a in range(0, i):
            print(cadena[a], end="")
        print("")
    return piramideCaracter(cadena, i+1)


if __name__ == '__main__':
    cadena = str(input("Ingresa la cadena:\t"))
    piramideCaracter(cadena, 0)
