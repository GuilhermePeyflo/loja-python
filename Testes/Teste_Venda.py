from Sistema.Venda import Venda
from datetime import datetime
import os


class TesteVenda:
    """
    Classe de testes da classe Venda.
    """

    def __init__(self):
        """
        Método para testar a classe Venda.
        Exclui os dados das vendas antes de realizar os testes.
        Gera produtos, itens de venda e vendas para realizar os testes.
        Testa se retorna uma lista vazia quando não houver vendas salvas.
        Testa se cadastra novas vendas.
        Testa se retorna uma lista com as vendas cadastradas.
        """
        try:
            os.remove("../BancoDados/vendas.txt")
        except:
            pass
        finally:
            produto1 = {"nome": "Produto 0", "codigo": "003", "preco": "27", "categoria": "Alimento"}
            produto2 = {"nome": "Produto 1", "codigo": "000", "preco": "27", "categoria":"Bebida"}
            produto3 = {"nome": "Produto 2", "codigo": "001", "preco": "27", "categoria":"Higiene"}
            itens1 = [produto1]
            itens2 = [produto1, produto2]
            itens3 = [produto1, produto2, produto3]

            venda = Venda()
            if not venda.listar_vendas():
                print("Teste Mostrar Lista Vendas vazia: Passou!")
            else:
                print("Teste Mostrar Lista Vendas vazia: Falhou!")

            nova_venda = {"data_hora":str(datetime.today()),"itens_venda":itens1,"total_venda":"27"}
            if venda.cadastrar_venda(nova_venda):
                print("Teste cadastrar nova venda: Passou!")
            else:
                print("Teste cadastrar nova venda: Falhou!")

            nova_venda = {"data_hora": str(datetime.today()), "itens_venda": itens2, "total_venda": "54"}
            if venda.cadastrar_venda(nova_venda):
                print("Teste cadastrar nova venda: Passou!")
            else:
                print("Teste cadastrar nova venda: Falhou!")

            nova_venda = {"data_hora": str(datetime.today()), "itens_venda": itens3, "total_venda": "81"}
            if venda.cadastrar_venda(nova_venda):
                print("Teste cadastrar nova venda: Passou!")
            else:
                print("Teste cadastrar nova venda: Falhou!")

            if venda.listar_vendas():
                print("Teste Mostrar Lista Vendas: Passou!")
            else:
                print("Teste Mostrar Lista Vendas: Falhou!")


if __name__ == "__main__":
    TesteVenda()
