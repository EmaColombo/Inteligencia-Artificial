from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import BaseViewer, ConsoleViewer, WebViewer

INITIAL = ()
FICHAS = [(0,0), (0,2),(0,4), (0,6),(1,4),(2,0), (3,1), (3,6), (3,7),(3,9),
    (4,0),(4,7), (4,8),(5,4), (5,9),(6,0),(6,5), (6,9), (7,0), (7,7),
    (8,2),(8,4), (8,9),(9,1), (9,4),(9,6),(9,7)]

def chequearAlrededores(state):
    cantidadFichas = 0
    fila, columna = state
    if fila > 0:
        if (fila -1, columna) in FICHAS:
            cantidadFichas += 1
    if fila < 9:
        if (fila + 1, columna) in FICHAS:
            cantidadFichas += 1
    if columna > 0:
        if (fila, columna -1) in FICHAS:
            cantidadFichas += 1
    if columna < 9:
        if (fila, columna +1) in FICHAS:
            cantidadFichas += 1
    return cantidadFichas

class HnefataflProblema(SearchProblem):

        def is_goal(self, state):
            goal = False
            fila, columna = state
            if fila == 0:
                goal = True
            elif fila == 9:
                goal = True
            elif columna == 0:
                goal = True
            elif columna == 9:
                goal = True
            return goal

        def cost(self, state1, action, state2):
            return 1

        #Calcula la distancia al borde mas cercano
        def heuristic(self, state):
            fila, columna = state
            distancias = []
            cantidad_Izq = columna
            cantidad_Der = 10 - columna
            cantidad_Arriba = fila
            cantidad_Abajo = 10 - fila
            distancias.append(cantidad_Abajo)
            distancias.append(cantidad_Arriba)
            distancias.append(cantidad_Izq)
            distancias.append(cantidad_Der)
            resultado = min(distancias)
            return resultado

	def actions(self, state):
            row_0, col_0 = state
            actions = []
            if row_0 > 0:
                if (row_0 -1, col_0) not in FICHAS:
                    if chequearAlrededores((row_0 - 1, col_0)) < 2:
                        actions.append(('Arriba ',(row_0 - 1, col_0)))
            if row_0 < 9:
                if (row_0 +1, col_0) not in FICHAS:
                    if chequearAlrededores((row_0 + 1, col_0)) < 2:
                        actions.append(('Abajo ',(row_0 + 1, col_0)))
            if col_0 > 0:
                if (row_0, col_0 -1) not in FICHAS:
                    if chequearAlrededores((row_0, col_0 - 1)) < 2:
                        actions.append(('Izquierda ',(row_0, col_0 - 1)))
            if col_0 < 9:
                if (row_0, col_0 +1) not in FICHAS:
                    if chequearAlrededores((row_0, col_0 + 1)) < 2:
                        actions.append(('Derecha ',(row_0, col_0 + 1)))
            return actions

	def result(self, state, action):
	    actualposition = state
	    row_0, col_0 = actualposition
	    name,(d_row, d_col) = action
	    row_n, col_n = (d_row, d_col)
	    actualposition = (row_n, col_n)
	    return actualposition


def resolver(metodo_busqueda, posicion_rey, controlar_estados_repetidos):

    INITIAL = posicion_rey
    problema = HnefataflProblema(posicion_rey)
    visor = BaseViewer()

    #Busqueda en amplitud
    if (metodo_busqueda == 'breadth_first'):
        resultado = breadth_first(problema, graph_search=controlar_estados_repetidos, viewer=visor)
        return resultado

    #Busqueda en profundidad
    if (metodo_busqueda == 'depth_first'):
        resultado = depth_first(problema, graph_search=controlar_estados_repetidos, viewer=visor)
        return resultado

    #Busqueda avara
    if (metodo_busqueda == 'greedy'):
        resultado = greedy(problema, graph_search=controlar_estados_repetidos, viewer=visor)
        return resultado

    #Busqueda A Estrella
    if (metodo_busqueda == 'astar'):
        resultado = astar(problema, graph_search=controlar_estados_repetidos, viewer=visor)
        return resultado

#   for action, state in resultado.path():
#        print action

#    print resultado.path()
#   print 'produndidad: ' + str(resultado.depth)

#    print state
#    print 'El costo es: ' + str(resultado.cost)
#    print visor.stats

#if __name__ == '__main__':
#    resolver('breadth_first', (5,3),True)