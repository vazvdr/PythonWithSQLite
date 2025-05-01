from datetime import date
from banco import Bn
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

if __name__ == "__main__":

    banco = BancoDeDados()
    banco.conectar()
    banco.criar_tabela()

pessoa1 = Pessoa(cpf=12345678900, nome="Vanderson", nascimento=date(1991, 1, 13), oculos=True)
banco.inserir_pessoa(pessoa1)

marca1  = Marca(id=1, nome="Fiat", sigla="FIA")
banco.inserir_marca(marca1)

veiculo1= Veiculo(placa="KMN-2030", cor="preto", proprietario=pessoa1, marca=marca1)
banco.inserir_veiculo(veiculo1)

print("Pessoas: ")
for pessoa in banco.buscar_todas_pessoas():
    print(pessoa)

print("\nMarcas: ")
for marca in banco.buscar_todas_marcas():
    print(marca)

print("\nVeículos: ")
for veiculo in banco.buscar_todos_veiculos():
    print(veiculo)

banco.fechar_conexao()