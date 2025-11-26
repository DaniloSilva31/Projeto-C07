import mysql.connector

class ProPlayer:
    def __init__(self, id_pro_player=None, nickname=None, usuario_id=None, equipe_nome=None):
        self.id_pro_player = id_pro_player
        self.nickname = nickname
        self.usuario_id = usuario_id
        self.equipe_nome = equipe_nome


class ProPlayerDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)

    # INSERT
    def inserir(self, player: ProPlayer):
        sql = "INSERT INTO pro_player (nickname, usuario_id_usuario, equipe_nome) VALUES (%s, %s, %s)"
        try:
            self.cursor.execute(sql, (player.nickname, player.usuario_id, player.equipe_nome))
            self.conn.commit()
        except Exception as e:
            print("Erro ao inserir:", e)

    # UPDATE
    def atualizar(self, player: ProPlayer):
        sql = "UPDATE pro_player SET nickname=%s, usuario_id_usuario=%s, equipe_nome=%s WHERE id_pro_player=%s"
        try:
            self.cursor.execute(sql, (player.nickname, player.usuario_id, player.equipe_nome, player.id_pro_player))
            self.conn.commit()
        except Exception as e:
            print("Erro ao atualizar:", e)

    # DELETE
    def deletar(self, id_pro_player):
        sql = "DELETE FROM pro_player WHERE id_pro_player=%s"
        try:
            self.cursor.execute(sql, (id_pro_player,))
            self.conn.commit()
        except Exception as e:
            print("Erro ao deletar:", e)

    # SELECT ALL
    def listar_todos(self):
        sql = "SELECT * FROM pro_player"
        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            return [ProPlayer(
                        id_pro_player=r['id_pro_player'],
                        nickname=r['nickname'],
                        usuario_id=r['usuario_id_usuario'],
                        equipe_nome=r['equipe_nome']
                    ) for r in resultados]
        except Exception as e:
            print("Erro ao listar:", e)
            return []

    # SELECT BY ID
    def buscar_por_id(self, id_pro_player):
        sql = "SELECT * FROM pro_player WHERE id_pro_player=%s"
        try:
            self.cursor.execute(sql, (id_pro_player,))
            r = self.cursor.fetchone()
            if r:
                return ProPlayer(
                    id_pro_player=r['id_pro_player'],
                    nickname=r['nickname'],
                    usuario_id=r['usuario_id_usuario'],
                    equipe_nome=r['equipe_nome']
                )
            return None
        except Exception as e:
            print("Erro ao buscar por id:", e)
            return None
