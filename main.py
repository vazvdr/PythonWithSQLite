from datetime import date
from bancodedados import BancoDeDados
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

if __name__ == "__main__":

    banco = BancoDeDados()
    banco.conectar()
    banco.criar_tabela()

pessoa1 = Pessoa(cpf=12345678900, nome="Vanderson", nascimento=date(1991, 1, 13), oculos=True)
banco.inserir_pessoa(pessoa1)

print(pessoa1)