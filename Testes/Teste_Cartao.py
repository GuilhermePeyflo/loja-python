from Sistema.Cartao import Cartao
import os


class TesteCartao:
    """
    Classe de testes da classe Cartao.
    """

    def __init__(self):
        """
        Método para realizar os testes da classe Cartão.
        Exclui os dados salvos antes de iniciar e carrega novos dados.
        Testa se retorna uma lista vazia quando não houver dados salvos.
        Testa se realiza com sucesso o desconto do saldo quando for informado um cartão válido.
        Testa se impede a compra caso o saldo for insuficiente.
        Testa se impede a compra caso a senha estiver incorreta.
        Testa se impede a compra caso o número for inválido.
        Testa se impede a compra caso o ano da validade expirou.
        Testa se impede a compra caso o mês da validade expirou.
        Testa se impede a compra caso o mês e o ano da validade expiraram.
        """
        try:
            os.remove("../BancoDados/cartoes.txt")
        except:
            pass
        finally:
            cartao = Cartao()
            if not cartao.listar_cartoes():
                print("Teste Mostrar Cartões: Falhou!")
            else:
                print("Teste Mostrar Cartões: Passou!")

            # {"numero":"1234","senha":"ABCD","validade":"04/2021","saldo":"10000"}
            if cartao.verificar_cartao("1234","ABCD",1000) == 0:
                ok = False
                for c in cartao.listar_cartoes():
                    if c["numero"] == "1234" and c["saldo"] == 9000:
                        ok = True
                if ok:
                    print("Teste Operação com cartão válido: Passou!")
                else:
                    print("Teste Operação com cartão válido: Falhou!")
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
    TesteCartao()
