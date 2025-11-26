class ProPlayerDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)

    def inserir(self, nickname, usuario_id, equipe_nome=None):
        try:
            sql = "INSERT INTO pro_player (nickname, usuario_id_usuario, equipe_nome) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (nickname, usuario_id, equipe_nome))
            self.conn.commit()
            print("Pro Player inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir Pro Player:", e)

    def atualizar(self, id_proplayer, nickname=None, usuario_id=None, equipe_nome=None):
        try:
            campos = []
            valores = []

            if nickname is not None:
                campos.append("nickname=%s")
                valores.append(nickname)

            if usuario_id is not None:
                campos.append("usuario_id_usuario=%s")
                valores.append(usuario_id)

            if equipe_nome is not None:
                campos.append("equipe_nome=%s")
                valores.append(equipe_nome)

            if not campos:
                print("Nenhum dado para atualizar!")
                return

            valores.append(id_proplayer)

            sql = "UPDATE pro_player SET " + ", ".join(campos) + " WHERE id_pro_player=%s"
            self.cursor.execute(sql, valores)
            self.conn.commit()
            print("Pro Player atualizado!")
        except Exception as e:
            print("Erro ao atualizar Pro Player:", e)

    def deletar(self, id_proplayer):
        try:
            sql = "DELETE FROM pro_player WHERE id_pro_player=%s"
            self.cursor.execute(sql, (id_proplayer,))
            self.conn.commit()
            print("Pro Player deletado!")
        except Exception as e:
            print("Erro ao deletar Pro Player:", e)

    def listar(self):
        try:
            self.cursor.execute("SELECT * FROM pro_player")
            return self.cursor.fetchall()
        except Exception as e:
            print("Erro ao listar Pro Players:", e)
            return []
