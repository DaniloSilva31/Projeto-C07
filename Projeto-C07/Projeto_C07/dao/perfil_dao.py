class PerfilUsuarioDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)

    def inserir(self, usuario_id, nickname, bio, pais, data_criacao):
        try:
            sql = """
            INSERT INTO Perfil_Usuario (usuario_id_usuario, nickname, bio, pais, data_criacao)
            VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(sql, (usuario_id, nickname, bio, pais, data_criacao))
            self.conn.commit()
            print("Perfil criado com sucesso!")
        except Exception as e:
            print("Erro ao inserir perfil:", e)

    def atualizar(self, usuario_id_usuario, nickname=None, bio=None, pais=None,data_criacao=None):
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
            if data_criacao is not None:
                campos.append("data_criacao=%s")
                valores.append(data_criacao)

            valores.append(usuario_id_usuario)

            sql = "UPDATE Perfil_Usuario SET " + ", ".join(campos) + " WHERE usuario_id_usuario=%s"
            self.cursor.execute(sql, valores)
            self.conn.commit()
            print("Perfil atualizado!")
        except Exception as e:
            print("Erro ao atualizar perfil:", e)

    def deletar(self, usuario_id_usuario):
        try:
            sql = "DELETE FROM Perfil_Usuario WHERE usuario_id_usuario=%s"
            self.cursor.execute(sql, (usuario_id_usuario,))
            self.conn.commit()
            print("Perfil deletado!")
        except Exception as e:
            print("Erro ao deletar perfil:", e)

    def listar_todos(self):
        sql = "SELECT * FROM torneio"
        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            return resultados  # <-- ADICIONE ISSO
        except Exception as e:
            print("Erro ao listar:", e)
            return []  # <-- evita erro no for

    def buscar_por_id(self, usuario_id_usuario):
        try:
            sql = "SELECT * FROM Perfil_Usuario WHERE usuario_id_usuario=%s"
            self.cursor.execute(sql, (usuario_id_usuario,))
            return self.cursor.fetchone()
        except Exception as e:
            print("Erro ao buscar perfil:", e)
            return None
