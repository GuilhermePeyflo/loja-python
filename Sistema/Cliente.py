from ast import literal_eval

def cadastrar_cliente(cliente):
    if verificar_cliente(cliente["cpf"]):
        return False
    else:
        with open("../BancoDados/clientes.txt", "a") as file:
            file.write(f"{cliente}\n")
        return True

def listar_clientes():
    clientes = list()
    try:
        with open("../BancoDados/clientes.txt", "r") as file:
            for c in list([i.strip() for i in file.readlines()]):
                cliente = literal_eval(c)
                clientes.append(cliente)
            return clientes
    except:
        print("Nenhum cliente cadastrado!")
    finally:
        return clientes

def excluir_cliente(cpf_cliente):
    if verificar_cliente(cpf_cliente):
        with open("../BancoDados/clientes.txt", "r+") as file:
            clientes = list()
            for c in list([i.strip() for i in file.readlines()]):
                cliente = literal_eval(c)
                if cpf_cliente != cliente["cpf"]:
                    clientes.append(cliente)
            file.seek(0)
            for c in clientes:
                file.write(f"{c}\n")
            file.truncate()
        return True
    else:
        return False

def verificar_cliente(cpf_cliente):
    clientes = listar_clientes()
    if clientes:
        for c in clientes:
            if c["cpf"] == cpf_cliente:
                return True
    else:
        return False