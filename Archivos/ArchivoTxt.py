def archivoTxt(nombre):
    a=open('archivo.txt','w')
    a.write(f"Hola soy {nombre} mundo de los archivos de texto")
    a.close()
archivoTxt("Jir")
def leerArchivoTxt():
    a=open('archivo.txt','r')
    print(a.read())
    a.close()
leerArchivoTxt()