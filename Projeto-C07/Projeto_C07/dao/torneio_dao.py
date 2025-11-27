import mysql.connector
from datetime import datetime

class Torneio:
    def __init__(self, nome=None, premiacao=None, data_inicio=None, data_fim=None, jogo_nome=None):
        self.nome = nome
        self.premiacao = premiacao
        self.data_inicio = data_inicio  # datetime.date
        self.data_fim = data_fim        # datetime.date
        self.jogo_nome = jogo_nome

class TorneioDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)

    # INSERT
    def inserir(self, torneio: Torneio):
        sql = "INSERT INTO torneio (nome, premiacao, data_inicio, data_fim, jogo_nome) VALUES (%s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (
                torneio.nome,
                torneio.premiacao,
                torneio.data_inicio,
                torneio.data_fim,
                torneio.jogo_nome
            ))
            self.conn.commit()
            print("Torneio inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir:", e)

    # UPDATE
    def atualizar(self, torneio: Torneio):
        sql = "UPDATE torneio SET premiacao=%s, data_inicio=%s, data_fim=%s, jogo_nome=%s WHERE nome=%s"
        try:
            self.cursor.execute(sql, (
                torneio.premiacao,
                torneio.data_inicio,
                torneio.data_fim,
                torneio.jogo_nome,
                torneio.nome
            ))
            self.conn.commit()
            print("Torneio atualizado com sucesso!")
        except Exception as e:
            print("Erro ao atualizar:", e)

    # DELETE
    def deletar(self, nome):
        sql = "DELETE FROM torneio WHERE nome=%s"
        try:
            self.cursor.execute(sql, (nome,))
            self.conn.commit()
            print("Torneio deletado com sucesso!")
        except Exception as e:
            print("Erro ao deletar:", e)

    # SELECT ALL
    def listar_todos(self):
        sql = "SELECT * FROM torneio"
        resultados = []
        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
        except Exception as e:
            print("Erro ao listar:", e)
            # aqui resultados continua sendo [] (lista vazia)

        return resultados

    # SELECT BY NOME
    def buscar_por_nome(self, nome):
        sql = "SELECT * FROM torneio WHERE nome=%s"
        try:
            self.cursor.execute(sql, (nome,))
            r = self.cursor.fetchone()
            if r:
                print(f"Nome: {r['nome']}, Premiação: {r['premiacao']}, "
                      f"Data Início: {r['data_inicio']}, Data Fim: {r['data_fim']}, Jogo: {r['jogo_nome']}")
            else:
                print("Torneio não encontrado.")
        except Exception as e:
            print("Erro ao buscar por nome:", e)
