from ast import literal_eval


class Cliente:
    """
    Classe para manipular dados dos clientes cadastrados.
    Permite cadastrar, listar e excluir clientes.
    """

    caminho_banco = "../BancoDados/clientes.txt"

    def __init__(self):
        """
        Método para criar o arquivo de banco dos clientes caso ainda não exista.
        """
        with open(self.caminho_banco, "a") as file:
            pass

    def cadastrar_cliente(self, cliente: dict) -> bool:
        """
        Método para cadastrar novos clientes.
        Caso o CPF não esteja cadastrado, um novo cliente será registrado no arquivo e retornará True.
        Caso o CPF já esteja cadastrado, retornará False.

        :param cliente: dict
        :return bool
        """
        if self.verificar_cliente(cliente["cpf"]):
            return False
        else:
            with open(self.caminho_banco, "a") as file:
                file.write(f"{cliente}\n")
            return True

    def listar_clientes(self) -> list:
        """
        Método para listar os clientes cadastrados.
        Verifica o arquivo e retorna uma lista de clientes no formato de dicionário.
        Caso ocorra erro na leitura do arquivo ou nenhum cliente esteja cadastrado, retorna uma lista vazia.

        :return list
        """
        clientes = list()
        try:
            with open(self.caminho_banco, "r") as file:
                for c in list([i.strip() for i in file.readlines()]):
                    cliente = literal_eval(c)
                    clientes.append(cliente)
                return clientes
        except:
            pass
        finally:
            return clientes

    def verificar_cliente(self, cpf_cliente: str) -> bool:
        """
        Método para verificar se o cliente já está cadastrado.
        Caso o CPF for encontrado no arquivo de dados, retorna True.
        Caso não for encontrado, retorna False.

        :param cpf_cliente: str
        :return bool
        """
        clientes = self.listar_clientes()
        if clientes:
            for c in clientes:
                if c["cpf"] == cpf_cliente:
                    return True
        else:
            return False

    def excluir_cliente(self, cpf_cliente: str) -> bool:
        """
        Método para excluir um cliente cadastrado.
        Caso o CPF estiver cadastrado, ele será excluído do arquivo e retornará True.
        Caso o CPF não esteja cadastrado, retornará False.

        :param cpf_cliente: str
        :return bool
        """
        if self.verificar_cliente(cpf_cliente):
            with open(self.caminho_banco, "r+") as file:
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
