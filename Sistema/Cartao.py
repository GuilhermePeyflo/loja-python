from ast import literal_eval
from datetime import date


class Cartao:
    """
    Classe para manipular os dados de cartões.
    Simula a máquina de cartão.
    Não permite cadastrar novos cartões e nem excluir cartões.
    """

    caminho_banco = "../BancoDados/cartoes.txt"

    def __init__(self):
        """
        Método para realizar o cadastro prévio de alguns cartões que poderão ser utilizados.
        Caso o arquivo já exista, nenhum dado será alterado.
        Caso não exista, o arquivo será criado e alguns cartões serão gerados.
        """
        try:
            with open(self.caminho_banco, "r") as file:
                pass
        except:
            with open(self.caminho_banco, "w") as file:
                cartao = {"numero":"1234","senha":"ABCD","validade":"04/2021","saldo":10000}
                file.write(f"{cartao}\n")
                cartao = {"numero": "5678", "senha": "EFGH", "validade": "08/2020", "saldo": 10}
                file.write(f"{cartao}\n")
                cartao = {"numero": "2468", "senha": "IGKL", "validade": "03/2021", "saldo": 1000}
                file.write(f"{cartao}\n")
                cartao = {"numero": "1357", "senha": "MNOP", "validade": "01/2020", "saldo": 100}
                file.write(f"{cartao}\n")

    def listar_cartoes(self) -> list:
        """
        Método para listar os cartões cadastrados.
        Realiza a leitura do arquivo e retorna uma lista com os dados da cada cartão cadastrado.
        Caso o arquivo não exista ou nenhum cartão esteja cadastrado, retorna uma lista vazia.

        :return list
        """
        cartoes = list()
        try:
            with open(self.caminho_banco, "r") as file:
                for c in list([i.strip() for i in file.readlines()]):
                    cartao = literal_eval(c)
                    cartoes.append(cartao)
                return cartoes
        except:
            pass
        finally:
            return cartoes

    def atualizar_saldo(self, numero_cartao: str, novo_saldo: float) -> bool:
        """
        Método para atualizar o saldo de um cartão.
        Realiza a leitura do arquivo, salvando os dados dos cartões que não forem solicitados para alteração.
        Quando encontrar o cartão com o número pesquisado, altera o seu saldo e salva no arquivo.
        Caso finalize com sucesso, retorna True.
        Caso ocorra algum problema, retorna False.

        :param numero_cartao: str
        :param novo_saldo: float
        :return bool
        """
        try:
            with open(self.caminho_banco, "r+") as file:
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

    def verificar_cartao(self, numero_cartao: str, senha_cartao: str, valor_compra: float) -> int:
        """
        Método para verificar o cartão.
        Caso o número informado não exista ou nenhum cartão seja encontrado, retorna 4.
        Caso o número informado exista, mas a senha esteja incorreta, retorna 3.
        Caso ambos o número e a senha estejam corretos, mas a validade do cartão tenha vencido, retorna 2.
        Caso número, senha e validade estejam válidos, mas o saldo seja insuficiente perante o valor da compra, retorna 1.
        Caso tudo esteja de acordo, será descontado o valor da compra do saldo e ele será atualizado, retornando 0.

        :param numero_cartao: str
        :param senha_cartao: str
        :param valor_compra: float
        :return int
        """
        cartoes = self.listar_cartoes()
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
                                self.atualizar_saldo(c["numero"], saldo_cartao - valor_compra)
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
