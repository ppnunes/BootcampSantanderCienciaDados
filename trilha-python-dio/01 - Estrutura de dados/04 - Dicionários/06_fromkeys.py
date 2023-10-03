# Cria chaves no seu dicionario sem vincular valor    OU
# cria um conjunto de chaves e coloca um valor padrão nela

resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)
