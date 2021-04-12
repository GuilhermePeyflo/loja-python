from Sistema.Cliente import Cliente
import os

try:
    os.remove("../BancoDados/clientes.txt")
except:
    print("erro")
finally:
    print(Cliente().listar_clientes())
    print(Cliente().cadastrar_cliente({"nome": "Thiago", "cpf": "000", "idade": "27"}))
    print(Cliente().cadastrar_cliente({"nome": "Joao", "cpf": "001", "idade": "27"}))
    print(Cliente().cadastrar_cliente({"nome": "Gustavo", "cpf": "002", "idade": "27"}))
    print(Cliente().cadastrar_cliente({"nome": "Thiago", "cpf": "000", "idade": "27"}))
    print(Cliente().listar_clientes())
    print(Cliente().excluir_cliente("001"))
    print(Cliente().excluir_cliente("004"))
    print(Cliente().listar_clientes())
    print(Cliente().cadastrar_cliente({"nome": "Joao", "cpf": "001", "idade": "27"}))
    print(Cliente().listar_clientes())