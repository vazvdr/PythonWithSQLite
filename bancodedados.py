import os
import sqlite3
from pessoa import Pessoa
from veiculo import Veiculo
from marca import Marca

class BancoDeDados:
    def __init__(self, nome_banco="banco.sqlite"):
        self.nome_banco = os.path.join(os.path.dirname(__file__), nome_banco)
        self.conn = None

        def conectar(self):
            try:
                self.conn = sqlite3.connect(self.nome_banco)
            except sqlite3.DatabaseError as e:
                print(f"Erro ao conectar com o banco de dados: {e}")

        def criar_tabela(self):
            self.criar_tabela_pessoa()
            self.criar_tabela_marca()
            self.criar_tabela_veiculo()

    def criar_tabela_pessoa(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Pessoa(
                        cpf INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        nascimento DATE,
                        oculos BOOLEAN
                    )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar a tabela pessoa: {e}")
            except sqlite3.ProgrammingError as cursor:
                print(f"O cursor está fechado: {cursor}")
    
    def criar_tabela_marca(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS MARCAR(
                    id INTERGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    sigla TEXT
                    )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar a tabela marca: {e}")
            except sqlite3.ProgrammingError as cursor:
                print(f"O cursor está fechado: {cursor}")

    def criar_tabela_veiculo(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS Veiculo(
                placa TEXT PRIMARY KEY,
                cor TEXT NOT NULL,
                cpf_proprietario INTEGER,
                id_marca INTEGER,
                FOREIGN KEY(cpf_proprietario) REFERENCES Pessoa(cpf),
                FOREIGN KEY(id_marca) REFERENCES Marca(id))"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar a tabela Veiculo: {e}")
            except sqlite3.ProgrammingError as cursor:
                print(f"O cursor está fechado: {cursor}")

    def inserir_pessoa(self, pessoa: Pessoa):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO Pessoa VALUES (?, ?, ?, ?)",
                (pessoa.cpf, pessoa.nome, pessoa.nascimento, pessoa.oculos),)
                    self.conn.commit()
                except sqlite3.Error as e:
                    print(f"Erro ao inserir pessoa: {e}")
    
    def inserir_veiculo(self, veiculo: Veiculo):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "INSERT INTO Veiculo VALUES (?, ?, ?, ?)",
                (
                    veiculo.placa,
                    veiculo.cor,
                    veiculo.proprietario.cpf,
                    veiculo.marca.id,
                ),
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao inserir veículo: {e}")

    def atualizar_pessoa(self, pessoa):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "UPDATE Pessoa SET nome=?, nascimento=?, oculos=? WHERE cpf=?",
                    (pessoa.nome, pessoa.nascimento, pessoa.oculos, pessoa.cpf),
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao atualizar pessoa: {e}")

    def apagar_veiculo(self, veiculo):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM Veiculo WHERE placa=?",
        (veiculo.placa,))
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao apagar veiculo: {e}")
    
    def buscar_todas_pessoas(self):
        pessoas = []
        if self.conn:
            try: 
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Pessoa")
                for row in cursor.fetchall():
                    cpf, nome, nascimento, oculos = row
                    pessoas.append(Pessoa(cpf, nome, nascimento, oculos,))
            except sqlite3.Error as e:
                print(f"Erro ao buscar pessoas")
        return pessoas

    def buscar_todos_veiculos(self):
        veiculos = []
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Veiculo")
                for row in cursor.fetchall():
                    placa, cor, cpf_proprietario, id_marca = row proprietario =
                    self.buscar_pessoa_por_cpf(cpf_proprietario)
                    marca = self.buscar_marca_por_id(id_marca)
                    veiculos.append(Veiculo(placa, cor, proprietario, marca))
            except sqlite3.Error as e:
                print(f"Erro ao buscar veículos: {e}")
            return veiculos

    def buscar_pessoa_por_cpf(self, cpf: int):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Pessoa WHERE cpf=?", (cpf,))
                row = cursor.fetchone()
                if row:
                    cpf, nome, nascimento, oculos = row
                    return Pessoa(cpf, nome, nascimento, oculos)
            except sqlite3.Error as e:
                print(f"Erro ao buscar pessoa por CPF: {e}")
            return None
    
    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.conn = None
