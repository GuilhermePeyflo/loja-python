from ast import literal_eval
from datetime import date
import os

def cadastrar_cartoes():
    try:
        os.remove("../BancoDados/cartoes.txt")
    except:
        pass
    finally:
        with open("../BancoDados/cartoes.txt", "a") as file:
            cartao = {"numero":"1234","senha":"ABCD","validade":"04/2021","saldo":"10000"}
            file.write(f"{cartao}\n")
            cartao = {"numero": "5678", "senha": "EFGH", "validade": "08/2020", "saldo": "10"}
            file.write(f"{cartao}\n")
            cartao = {"numero": "2468", "senha": "IGKL", "validade": "03/2021", "saldo": "1000"}
            file.write(f"{cartao}\n")
            cartao = {"numero": "1357", "senha": "MNOP", "validade": "01/2020", "saldo": "100"}
            file.write(f"{cartao}\n")

def listar_cartoes():
    cartoes = list()
    try:
        with open("../BancoDados/cartoes.txt", "r") as file:
            for c in list([i.strip() for i in file.readlines()]):
                cartao = literal_eval(c)
                cartoes.append(cartao)
            return cartoes
    except:
        pass
    finally:
        return cartoes

def atualizar_saldo(numero_cartao, novo_saldo):
    try:
        with open("../BancoDados/cartoes.txt", "r+") as file:
            cartoes = list()
            for c in list([i.strip() for i in file.readlines()]):
                cartao = literal_eval(c)
                if numero_cartao == cartao["numero"]:
                    cartao["saldo"] = novo_saldo
                cartoes.append(cartao)
            file.seek(0)
            for c in cartoes:
                file.write(f"{c}\n")
            file.truncate()
        return True
    except:
        return False

def verificar_cartao(numero_cartao, senha_cartao, valor_compra):
    cartoes = listar_cartoes()
    for c in cartoes:
        if numero_cartao == c["numero"]:
            if senha_cartao == c["senha"]:
                mes_atual = int(date.today().strftime("%m"))
                ano_atual = int(date.today().strftime("%Y"))
                validade_cartao = c["validade"].split("/")
                mes_cartao = int(validade_cartao[0])
                ano_cartao = int(validade_cartao[1])
                if ano_cartao >= ano_atual:
                    if mes_cartao >= mes_atual:
                        saldo_cartao = int(c["saldo"])
                        if saldo_cartao >= valor_compra:
                            atualizar_saldo(c["numero"], saldo_cartao - valor_compra)
                            return 0
                        else:
                            return 1
                    else:
                        return 2
                else:
                    return 2
            else:
                return 3
    return 4