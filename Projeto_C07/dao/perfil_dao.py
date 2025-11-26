class PerfilUsuarioDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)

    def inserir(self, usuario_id, nickname, bio, pais):
        try:
            sql = """
            INSERT INTO PerfilUsuario (usuario_id, nickname, bio, pais)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(sql, (usuario_id, nickname, bio, pais))
            self.conn.commit()
            print("Perfil criado com sucesso!")
        except Exception as e:
            print("Erro ao inserir perfil:", e)

    def atualizar(self, id_perfil, nickname=None, bio=None, pais=None):
        try:
            campos = []
            valores = []

            if nickname is not None:
                campos.append("nickname=%s")
                valores.append(nickname)
            if bio is not None:
                campos.append("bio=%s")
                valores.append(bio)
            if pais is not None:
                campos.append("pais=%s")
                valores.append(pais)

            valores.append(id_perfil)

            sql = "UPDATE PerfilUsuario SET " + ", ".join(campos) + " WHERE id=%s"
            self.cursor.execute(sql, valores)
            self.conn.commit()
            print("Perfil atualizado!")
        except Exception as e:
            print("Erro ao atualizar perfil:", e)

    def deletar(self, id_perfil):
        try:
            sql = "DELETE FROM PerfilUsuario WHERE id=%s"
            self.cursor.execute(sql, (id_perfil,))
            self.conn.commit()
            print("Perfil deletado!")
        except Exception as e:
            print("Erro ao deletar perfil:", e)

    def listar_todos(self):
        try:
            self.cursor.execute("SELECT * FROM PerfilUsuario")
            return self.cursor.fetchall()
        except Exception as e:
            print("Erro ao listar perfis:", e)
            return []

    def buscar_por_id(self, id_perfil):
        try:
            sql = "SELECT * FROM PerfilUsuario WHERE id=%s"
            self.cursor.execute(sql, (id_perfil,))
            return self.cursor.fetchone()
        except Exception as e:
            print("Erro ao buscar perfil:", e)
            return None
