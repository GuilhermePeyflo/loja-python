import Produto

def cadastrar_categoria(nome_categoria):
    if verificar_categoria(nome_categoria):
        return False
    else:
        with open("../BancoDados/categorias.txt", "a") as file:
            file.write(f"{nome_categoria}\n")
        return True

def listar_categorias():
    categorias = list()
    with open("../BancoDados/categorias.txt", "r") as file:
        for c in list([i.strip() for i in file.readlines()]):
            categorias.append(c)
    return categorias

def excluir_categoria(nome_categoria):
    if verificar_categoria(nome_categoria):
        with open("../BancoDados/categorias.txt", "r+") as file:
            categorias = list()
            for c in list([i.strip() for i in file.readlines()]):
                if nome_categoria != c:
                    categorias.append(c)
            file.seek(0)
            for c in categorias:
                file.write(f"{c}\n")
            file.truncate()
        produtos = Produto.pesquisar_produtos(nome_categoria)
        for p in produtos:
            p["categoria"] = "None"
            Produto.alterar_produto(p)
        return True
    else:
        return False

def verificar_categoria(nome_categoria):
    encontrado = False
    categorias = listar_categorias()
    if len(categorias) > 0:
        for c in categorias:
            if nome_categoria == c:
                encontrado = True
    return encontrado