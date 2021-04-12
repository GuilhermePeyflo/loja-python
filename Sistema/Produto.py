from ast import literal_eval

def cadastrar_produto(produto):
    if verificar_produto(produto["codigo"]):
        return False
    else:
        with open("../BancoDados/produtos.txt", "a") as file:
            file.write(f"{produto}\n")
        return True

def listar_produtos():
    produtos = list()
    try:
        with open("../BancoDados/produtos.txt", "r") as file:
            for p in list([i.strip() for i in file.readlines()]):
                produto = literal_eval(p)
                produtos.append(produto)
            return produtos
    except:
        print("Nenhum produto cadastrado!")
    finally:
        return produtos

def pesquisar_produtos(nome_categoria):
    produtos = list()
    try:
        with open("../BancoDados/produtos.txt", "r") as file:
            for p in list([i.strip() for i in file.readlines()]):
                produto = literal_eval(p)
                if produto["categoria"] == nome_categoria:
                    produtos.append(produto)
            return produtos
    except:
        print("Nenhum produto cadastrado!")
    finally:
        return produtos

def alterar_produto(produto_alterado):
    if verificar_produto(produto_alterado["codigo"]):
        with open("../BancoDados/produtos.txt", "r+") as file:
            produtos = list()
            for p in list([i.strip() for i in file.readlines()]):
                produto = literal_eval(p)
                if produto_alterado["codigo"] == produto["codigo"]:
                    produto["nome"] = produto_alterado["nome"]
                    produto["preco"] = produto_alterado["preco"]
                    produto["categoria"] = produto_alterado["categoria"]
                produtos.append(produto)
            file.seek(0)
            for p in produtos:
                file.write(f"{p}\n")
            file.truncate()
        return True
    else:
        return False

def excluir_produto(codigo_produto):
    if verificar_produto(codigo_produto):
        with open("../BancoDados/produtos.txt", "r+") as file:
            produtos = list()
            for p in list([i.strip() for i in file.readlines()]):
                produto = literal_eval(p)
                if codigo_produto != produto["codigo"]:
                    produtos.append(produto)
            file.seek(0)
            for p in produtos:
                file.write(f"{p}\n")
            file.truncate()
        return True
    else:
        return False

def verificar_produto(codigo_produto):
    produtos = listar_produtos()
    if produtos:
        for p in produtos:
            if p["codigo"] == codigo_produto:
                return True
    else:
        return False