#Ejercicio con busqueda a profundidad
from ast import While
from re import A
from arbol import Nodo
def buscar_solucion_DFS(estado_inicial,solucion):
    solucionado=False
    nodos_visitados=[]
    nodos_frontera=[]
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while(not solucionado) and len(nodos_frontera)!=0 :
        nodo=nodos_frontera.pop
        #extraer nodo y añadirlo a visitados
        if(nodo.get_Datos()==solucion):
            #Solucion encontrada
            solucionado=True
            return nodo
        else:
            #Expandir nodos hijos
            dato_nodo=nodo.get_Datos()
            