from datetime import date
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

pessoa1 = Pessoa(cpf=12345678900, nome="Vanderson", nascimento=date(1991, 1, 13), oculos=True)

marca1  = Marca(id=1, nome="Fiat", sigla="FIA")

veiculo1= Veiculo(placa="KMN-2030", cor="preto", proprietario=pessoa1, marca=marca1)

print(pessoa1)