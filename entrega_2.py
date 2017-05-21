from simpleai.search import (CspProblem, backtrack, min_conflicts, MOST_CONSTRAINED_VARIABLE,LEAST_CONSTRAINING_VALUE,HIGHEST_DEGREE_VARIABLE)

variables = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']

dominios = {variable: ['motor', 'bahias_carga', 'SVE', 'escudo', 'bateria', 'laser', 'cabina'] for variable in variables}


conexiones = (('A','B'),('A','C'),('B','D'),('C','D'),('C','E'),('D','F'),('E','G'),('F','H'),('G','H'),('G','I'),('H','I'),('I','J'),
				('J','K'),('K','L'),('L','M'),('L','N'),('L','P'),('P','O'),('P','Q'))

conexiones_por_variable = (('A','B','C'), ('B','A','D'), ('C','A','D','E'), ('D','B','C','F'), ('E','C','G'), ('F','D','H'), 
	('G','E','H','I'), ('H','F','G'), ('I','G','H','J'), ('J','I','K'),('K','J','L'), ('L','K','M','N','P'), ('M','L'), ('N','L'), 
	('O','P'), ('P','L','O','Q'), ('Q','P'))

consumen_bateria = ['SVE', 'cabina', 'laser', 'escudo']



for variable_no_motor in list('ABCDHGIJK'):
	dominios[variable_no_motor].remove('motor')

def conexion_bateria_laser(variables, valores):
	if valores[0] == 'laser' and valores[1] == 'bateria':
		return False
	if valores[0] == 'bateria' and valores[1] == 'laser':
		return False
	return True

def conexion_cabinas_motores(variables, valores):
	if valores[0] == 'cabina' and valores[1] == 'motor':
		return False
	if valores[0] == 'motor' and valores[1] == 'cabina':
		return False
	return True

def conexion_distintas(variables, valores):
	if valores[0] == valores[1]:
		return False
	return True

def conexion_escudo_SVE(variables, valores):
	if valores[0] == 'escudo' and valores[1] == 'SVE':
		return False
	if valores[0] == 'SVE' and valores[1] == 'escudo':
		return False
	return True

def conexion_bahia_carga_cabina(variables, valores):
	if 'bahias_carga' == valores[0]:
		if 'cabina' not in valores:
			return False
	return True

def conexion_sistemas_bateria(variables, valores):
	indice = 0
	cantidad = 0
	if valores[0] == 'bateria':
		for valor in valores:
			if indice > 0:
				if valores[int(indice)] in consumen_bateria:
					cantidad += 1
			indice += 1
		if cantidad > 1:
			return True
		else:
			return False
	return True

def conexion_SVE_cabina(variables, valores):
	if 'SVE' == valores[0]:
		if 'cabina' not in valores:
			return False
	return True

restricciones = []
for conexion in conexiones:
	restricciones.append((conexion, conexion_bateria_laser))
	restricciones.append((conexion, conexion_cabinas_motores))
	restricciones.append((conexion, conexion_distintas))
	restricciones.append((conexion, conexion_escudo_SVE))

for conexion2 in conexiones_por_variable:
	restricciones.append((conexion2, conexion_sistemas_bateria))
	restricciones.append((conexion2, conexion_SVE_cabina))
	restricciones.append((conexion2, conexion_bahia_carga_cabina))

def resolver(metodo_busqueda, iteraciones):
    problema = CspProblem(variables, dominios, restricciones)
    if metodo_busqueda == "backtrack":
        resultado = backtrack(problema)
        return resultado
    if metodo_busqueda == "min_conflicts":
       	resultado = min_conflicts(problema, iterations_limit=iteraciones)
       	return resultado

#resolver("backtrack", 500)

#resultado = resolver("backtrack", None)
#print resultado
