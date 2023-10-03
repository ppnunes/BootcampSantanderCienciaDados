# Os dicionarios são um conjunto não ordenado de pares chave:valor onde essa chaves têm valores únicos. Os valores podem ser mutaveis ou imutaveis. Usamos chaves ou a classe dict

pessoa = {"nome": "Guilherme", "idade": 28}     #nesse dicionario a chave "nome" tem valor "Guilherme" e a chave "idade" tem valor "28"
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)   
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
