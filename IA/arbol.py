class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.coste = None
        self.setHijos = (hijos)

    def set_Hijos(self, hijos): #Asigna al nodo la lista de hijos que osn pasados con parametro
        self.hijos = hijos
        if self.hijos != None:
            for h in self.hijos:
                h.padre = self

    def get_Hijos(self): #Retorna una lista con los hijos del nodo
        return self.hijos

    def get_Padre(self): #Retorna el nodo padre
        return self.padre

    def set_Padre(self, padre): #Asigna el nodo padre de este nodo
        self.padre = padre

    def set_Datos(self, datos): #Asigna un dato a un nodo
        self.datos = datos

    def get_Datos(self): #Devuelve el dato almacenado de un nodo
        return self.datos

    def set_Coste(self, coste): #Asigna un peso al nodo dentro del arbol
        self.coste = coste

    def get_Coste(self): #Devuelve el peso del nodo dentro del arbol
        return self.coste

    def igual(self, nodo): #Devuelve True si el dato contenido en el nodo es igual al nodo pasado por parametro
        if self.get_Datos() == nodo.get_Datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos): #Devuelve True si el dato contenido en el nodo es igual a algunoi de los nodos contenidos en la lista de nodos pasada por parametros 
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista

    def __str__(self):
        return str(self.get_Datos())
