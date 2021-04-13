from Sistema.Cartao import Cartao
import os

class Teste_Cartao:
    """
    Classe de testes da classe Cartao.
    """

    def __init__(self):
        try:
            os.remove("../BancoDados/cartoes.txt")
        except:
            print("erro")
        finally:
            cartao = Cartao()
            if not cartao.listar_cartoes():
                print("Teste Mostrar Cartões: Falhou!")
            else:
                print("Teste Mostrar Cartões: Passou!")

            # {"numero":"1234","senha":"ABCD","validade":"04/2021","saldo":"10000"}
            if cartao.verificar_cartao("1234","ABCD",1000) == 0:
                print("Teste Operação com cartão válido: Passou!")
            else:
                print("Teste Operação com cartão válido: Falhou!")

            if cartao.verificar_cartao("1234","ABCD",10000) != 1:
                print("Teste com valor de compra superior a saldo: Falhou!")
            else:
                print("Teste com valor de compra superior a saldo: Passou!")

            if cartao.verificar_cartao("1234","ABCDE",100) != 3:
                print("Teste com senha incorreta: Falhou")
            else:
                print("Teste com senha incorreta: Passou")

            if cartao.verificar_cartao("12345","ABCD",100) != 4:
                print("Teste com número inválido: Falhou!")
            else:
                print("Teste com número inválido: Passou!")

            # {"numero": "5678", "senha": "EFGH", "validade": "08/2020", "saldo": "10"}
            if cartao.verificar_cartao("5678","EFGH",10) != 2:
                print("Teste com validade expirada: Data cartão(08/2020) | Data atual(04/2021): Falhou!")
            else:
                print("Teste com validade expirada: Data cartão(08/2020) | Data atual(04/2021): Passou!")

            # {"numero": "2468", "senha": "IGKL", "validade": "03/2021", "saldo": "1000"}
            if cartao.verificar_cartao("2468","IGKL",10) != 2:
                print("Teste com validade expirada: Data cartão(03/2021) | Data atual(04/2021): Falhou!")
            else:
                print("Teste com validade expirada: Data cartão(03/2021) | Data atual(04/2021): Passou!")

            # {"numero": "1357", "senha": "MNOP", "validade": "01/2020", "saldo": "100"}
            if cartao.verificar_cartao("1357", "MNOP", 10) != 2:
                print("Teste com validade expirada: Data cartão(01/2020) | Data atual(04/2021): Falhou!")
            else:
                print("Teste com validade expirada: Data cartão(01/2020) | Data atual(04/2021): Passou!")


if __name__ == "__main__":
    Teste_Cartao()
