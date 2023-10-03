# A diferença entre difference e symmetric difference é que ela retorna todos os elementos que não fazem parte da intersecçao dos conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)
