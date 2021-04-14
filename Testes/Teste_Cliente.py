from Sistema.Cliente import Cliente
import os


class TesteCliente:
    """
    Classe para testes da classe Cliente.
    """

    def __init__(self):
        """
        Método para testar a classe Cliente.
        Exclui os dados de clientes antes de realizar os testes.
        Testa se retorna uma lista vazia quando não houver clientes salvos.
        Testa se cadastra novos clientes.
        Testa se impede o cadastro de clientes com CPF repetidos.
        Testa se retorna uma lista com os clientes cadastrados.
        Testa se exclui um cliente existente.
        Testa se impede a exclusão de um cliente inexistente.
        Testa se cadastra um novo cliente após a exclusão dele.
        """

    try:
        os.remove("../BancoDados/clientes.txt")

    except:
        pass
    finally:
        cliente = Cliente()
        if not cliente.listar_clientes():
            print("Teste Mostrar Lista Clientes vazia: Passou!")
        else:
            print("Teste Mostrar Lista Clientes vazia: Falhou!")

        if cliente.cadastrar_cliente({"nome": "Thiago", "cpf": "000", "idade": "27"}):
            print("Teste cadastrar novo cliente: Passou!")
        else:
            print("Teste cadastrar novo cliente: Falhou!")

        if cliente.cadastrar_cliente({"nome": "Joao", "cpf": "001", "idade": "27"}):
            print("Teste cadastrar novo cliente: Passou!")
        else:
            print("Teste cadastrar novo cliente: Falhou!")

        if cliente.cadastrar_cliente({"nome": "Gustavo", "cpf": "002", "idade": "27"}):
            print("Teste cadastrar novo cliente: Passou!")
        else:
            print("Teste cadastrar novo cliente: Falhou!")

        if cliente.cadastrar_cliente({"nome": "Thiago", "cpf": "000", "idade": "27"}):
            print("Teste cadastrar cliente existente: Falhou!")
        else:
            print("Teste cadastrar novo cliente: Passou!")

        if cliente.listar_clientes():
            print("Teste Mostrar Lista Clientes: Passou!")
        else:
            print("Teste Mostrar Lista Clientes: Falhou!")

        if cliente.excluir_cliente("001"):
            print("Teste excluir cliente existente: Passou!")
        else:
            print("Teste excluir cliente existente: Falhou!")

        if cliente.excluir_cliente("004"):
            print("Teste excluir cliente inexistente: Falhou!")
        else:
            print("Teste excluir cliente inexistente: Passou!")

        if cliente.cadastrar_cliente({"nome": "Joao", "cpf": "001", "idade": "27"}):
            print("Teste cadastrar cliente após exclusão: Passou!")
        else:
            print("Teste cadastrar cliente após exclusão: Falhou!")


if __name__ == "__main__":
    TesteCliente()
