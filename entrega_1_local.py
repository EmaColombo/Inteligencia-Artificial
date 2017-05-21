from random import randint
from simpleai.search import SearchProblem, hill_climbing, beam, hill_climbing_random_restarts, simulated_annealing, hill_climbing_stochastic
from simpleai.search.viewers import ConsoleViewer, WebViewer, BaseViewer

INITIAL = ((0,0), (0,1),(0,2), (0,3),(0,4),(0,5), (0,6), (0,7), (0,8),(0,9),
    (1,0), (1,1),(1,2), (1,3),(1,4),(1,5), (1,6), (1,7), (1,8),(1,9),
    (2,0), (2,1),(2,2), (2,3),(2,4),(2,5), (2,6), (2,7), (2,8),(2,9))


def chequearAlrededores(fila, columna, state):
    puntaje = 0
    if (fila, columna) not in state:

        if fila > 0:
            if (fila -1, columna) in state:
                puntaje += 1
        if fila < 9:
            if (fila + 1, columna) in state:
                puntaje += 1
        if columna > 0:
            if (fila, columna -1) in state:
                puntaje += 1
        if columna < 9:
            if (fila, columna +1) in state:
                puntaje += 1

    if puntaje > 1:
        if fila in (0,9) or columna in (0,9):
            puntaje = 3
        else:
            puntaje = 1
    else:
        puntaje = 0
    return puntaje


class HnefataflProblema(SearchProblem):

    def actions(self, state):
        action = []
        vacias = []

        for fila in range(0,10):
            for columna in range(0,10):
                if(fila, columna) not in state:
                    vacias.append((fila,columna))

        for peon in state:
            for casilla in vacias:
                action.append((peon,casilla))
        return action


    def result(self, state, action):
        state = list(list(x) for x in state)
        state.remove(list(action[0]))
        state.append(action[1])
        return tuple(tuple(x) for x in state)

    def value(self, state):
        totalPuntos = 0
        for fila in range(0,10):
            for columna in range(0,10):
                totalPuntos += chequearAlrededores(fila,columna, state)
        return totalPuntos

    def generate_random_state(self):
        Lista = ()
        while len(Lista) < 30:
            fila = randint(0,9)
            columna = randint(0,9)
            estado = (fila,columna)
            if estado not in Lista:
                Lista = Lista + ((fila, columna),)
        return Lista


def resolver(metodo_busqueda, iteraciones, haz, reinicios):


    visor = ConsoleViewer()

 
    if (metodo_busqueda == 'hill_climbing'):
        resultado = hill_climbing(problem=HnefataflProblema(INITIAL), iterations_limit=iteraciones)
        return resultado

   
    if (metodo_busqueda == 'hill_climbing_stochastic'):
        resultado = hill_climbing_stochastic(problem=HnefataflProblema(INITIAL), iterations_limit=iteraciones)
        return resultado


    if (metodo_busqueda == 'beam'):
        resultado = beam(problem=HnefataflProblema(None), beam_size=haz, iterations_limit=iteraciones)
        return resultado

    
    if (metodo_busqueda == 'hill_climbing_random_restarts'):
        resultado = hill_climbing_random_restarts(problem=HnefataflProblema(None), restarts_limit=reinicios, iterations_limit=iteraciones)
        return resultado

    if (metodo_busqueda == 'simulated_annealing'):
        resultado = simulated_annealing(problem=HnefataflProblema(INITIAL), iterations_limit=iteraciones)
        return resultado


