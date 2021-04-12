from ast import literal_eval


class Venda:
    """
    Classe para manipular dados das vendas efetuadas.
    Permite cadastrar e listar vendas finalizadas.
    """

    caminho_banco = "../BancoDados/vendas.txt"

    def __init__(self):
        """
        Método para criar o arquivo de banco das vendas caso ainda não exista.
        """
        with open(self.caminho_banco, "a") as file:
            pass

    def cadastrar_venda(self, venda: dict):
        """
        Método para cadastrar uma nova venda finalizada.
        """
        with open(self.caminho_banco, "a") as file:
            file.write(f"{venda}\n")

    def listar_vendas(self) -> list:
        """
        Método para listar as vendas cadastradas.
        Verifica o arquivo e retorna uma lista de vendas no formato de dicionário.
        Caso ocorra erro na leitura do arquivo ou nenhuma venda esteja cadastrada, retorna uma lista vazia.

        :return list
        """
        vendas = list()
        try:
            with open(self.caminho_banco, "r") as file:
                for v in list([i.strip() for i in file.readlines()]):
                    venda = literal_eval(v)
                    vendas.append(venda)
                return vendas
        except:
            pass
        finally:
            return vendas
