import mysql.connector
from datetime import datetime, date


class Torneio:
    def __init__(self, nome=None, premiacao=None, data_inicio=None, data_fim=None, jogo_nome=None):
        
        self.data_inicio = self._converter_data(data_inicio)
        self.data_fim = self._converter_data(data_fim)

        self.nome = nome
        self.premiacao = premiacao
        self.jogo_nome = jogo_nome

    def _converter_data(self, data):
        """Converte 'YYYY-MM-DD' para datetime.date, ou deixa None."""
        if data is None or data == "":
            return None
        
        if isinstance(data, date):
            return data  
        
        try:
            return datetime.strptime(data, "%Y-%m-%d").date()
        except:
            return None


class TorneioDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)

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

    def deletar(self, nome):
        sql = "DELETE FROM torneio WHERE nome=%s"
        try:
            self.cursor.execute(sql, (nome,))
            self.conn.commit()
            print("Torneio deletado com sucesso!")
        except Exception as e:
            print("Erro ao deletar:", e)

    def listar_todos(self):
        sql = "SELECT * FROM torneio"
        resultados = []

        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()

            for r in resultados:
                if isinstance(r["data_inicio"], date):
                    r["data_inicio"] = r["data_inicio"].strftime("%Y/%m/%d")
                if isinstance(r["data_fim"], date):
                    r["data_fim"] = r["data_fim"].strftime("%Y/%m/%d")

        except Exception as e:
            print("Erro ao listar:", e)
        
            return resultados
    def listar_torneios_com_jogo(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT t.nome AS torneio, t.premiacao, t.data_inicio, t.data_fim, j.nome AS jogo
            FROM torneio t
            JOIN jogo j ON t.jogo_nome = j.nome;
        """)
        return cursor.fetchall()

    def listar_torneios_com_equipes_e_jogadores(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT t.nome AS torneio, i.equipe_nome AS equipe, pr.id_pro_player, pr.nickname AS proplayer
            FROM torneio t
            JOIN inscricao i ON i.torneio_nome = t.nome
            LEFT JOIN pro_player pr ON pr.equipe_nome = i.equipe_nome
            ORDER BY t.nome, i.equipe_nome;
        """)
        return cursor.fetchall()
        