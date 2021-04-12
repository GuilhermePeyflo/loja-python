from ast import literal_eval

def cadastrar_venda(venda):
    with open("../BancoDados/vendas.txt", "a") as file:
        file.write(f"{venda}\n")

def listar_vendas():
    vendas = list()
    try:
        with open("../BancoDados/vendas.txt", "r") as file:
            for v in list([i.strip() for i in file.readlines()]):
                venda = literal_eval(v)
                vendas.append(venda)
            return vendas
    except:
        print("Nenhuma venda cadastrada!")
    finally:
        return vendas