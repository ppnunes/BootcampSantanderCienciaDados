# Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor list, a função range ou colocando valores separados por vírgula dentro de colchetes.

frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

# Cada letra de "python"é um elemento da lista:
letras = list("python")
print(letras)

# Essa lista cria um elemento para cada item no range de 0 a 10:
numeros = list(range(10))
print(numeros)

# Lista com os atributos de um carro:
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)


# Podemos acessar os valores de uma lista usando indices:

