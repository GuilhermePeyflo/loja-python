from Sistema.Cartao import Cartao
import os

try:
    os.remove("../BancoDados/cartoes.txt")
except:
    print("erro")
finally:
    cartao = Cartao()
    print(cartao.listar_cartoes())
    # {"numero":"1234","senha":"ABCD","validade":"04/2021","saldo":"10000"}
    print(cartao.verificar_cartao("1234","ABCD",1000))
    print(cartao.verificar_cartao("1234","ABCD",10000))
    print(cartao.verificar_cartao("1234","ABCDE",100))
    print(cartao.verificar_cartao("12345","ABCD",100))
    # {"numero": "5678", "senha": "EFGH", "validade": "08/2020", "saldo": "10"}
    print(cartao.verificar_cartao("5678","EFGH",10))
    # {"numero": "2468", "senha": "IGKL", "validade": "03/2021", "saldo": "1000"}
    print(cartao.verificar_cartao("2468","IGKL",10))
    # {"numero": "1357", "senha": "MNOP", "validade": "01/2020", "saldo": "100"}
    print(cartao.verificar_cartao("1357", "MNOP", 10))
