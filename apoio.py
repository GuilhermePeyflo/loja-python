# Criação de um dicionário
"""
dicio = {}
ou
dicio = dict()
"""
dicio = {"chave":"valor"}

lista1 = [1, 2, 3]
dicio = {"minha_lista": lista1}


"""
!!! Caso haja chaves duplicadas, só a última poderá ser acessada
"""


# Acessando itens de um dicionário
dicio = {"nome": "Gustavo", "idade": 100}

dicio["nome"] # Retorna "Gustavo"
# ou
dicio.get("nome") # Retorna


# Usando len() irá retornar quantos chave-valor o dicionário tem
dicio = {"nome": "Gustavo", "idade": 100}
len(dicio) # Retorna 2


# Usando keys()
dicio = {"nome": "Gustavo", "idade": 100}
dicio.keys() # Retorna dict_keys(['nome', 'idade'])
# keys() retorna um objeto dict_keys, logo não pode ser acessado por index, porém pode ser percorrido em um 'for'


# Usando values()
dicio = {"nome": "Gustavo", "idade": 100}
dicio.values() # Retorna dict_keys(['Gustavo', '100'])
# valeus() retorna um objeto dict_keys, logo não pode ser acessado por index, porém pode ser percorrido em um 'for'


# Usando items()
dicio = {"nome": "Gustavo", "idade": 100}
dicio.items() # Retorna dict_items([('nome', 'Gustavo'), ('idade', 100)])
# items() retorna um objeto dict_keys, logo não pode ser acessado por index, porém pode ser percorrido em um 'for'


# Verificando se uma chave existe
dicio = {"nome": "Gustavo", "idade": 100}
"nome" in dicio # Retorna True
"cpf" in dicio # Retorna False


# Mudando um valor do dicionário
dicio = {"nome": "Gustavo", "idade": 100}

dicio["nome"] = "Amanda"
# ou
dicio.update({"nome": "Amanda", "idade": 18})
# O método update() permite que mais de um valor possa ser mudado


# Adicionando itens
dicio = {"nome": "Gustavo", "idade": 100}
# Adicionar um novo item, é basicamente alterar algo que não existe

dicio["sobrenome"] = "Vergilio" # A chave sobrenome não existe, então ela é criada
# ou
dicio.update({"sobrenome": "Vergilio", "altura": 1.8})
# O método update() permite que mais de um valor possa ser mudado


# Removendo um item do dicionário
dicio = {"nome": "Gustavo", "idade": 100}

dicio.pop("nome")
# ou
del dicio["nome"]


# Usando clear()
dicio = {"nome": "Gustavo", "idade": 100}
dicio.clear() # Deixa o dicionário vazio {}


# Percorrendo um dicionário
dicio = {"nome": "Gustavo", "idade": 100}

for i in dicio:
    i # Retornará "nome", depois "idade"

for i in dicio:
    dicio[i] # Retornará "Gustavo", depois 100


# Percorrendo com keys()
dicio = {"nome": "Gustavo", "idade": 100}

for i in dicio.keys():
    i  # Retornará "nome", depois "idade"


# Percorrendo com values()
dicio = {"nome": "Gustavo", "idade": 100}

for i in dicio.values():
    i  # Retornará "Gustavo", depois 100


# Percorrendo com items()
dicio = {"nome": "Gustavo", "idade": 100}

for key, value in dicio.items():
    key  # Retornará "nome", depois "idade"
    value # Retornará "Gustavo", depois 100


# Usando copy()
dicio = {"nome": "Gustavo", "idade": 100}
dicio.copy() # Retorna uma cópia do dicicionário


# Exemplo de dicionário dentro de dicionário

pessoas = {
    "pessoa1": {"nome": "Gustavo","idade": 100},
    "pessoa2": {"nome": "Maria","idade": 18},
    "pessoa3": {"nome": "Amanda","idade": 16},
    "pessoa4": {"nome": "Vitória","idade": 18}
}


