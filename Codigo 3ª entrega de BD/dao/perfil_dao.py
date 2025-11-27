from datetime import datetime, date

class PerfilUsuarioDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)


    def _converter_data(self, data):
        """Converte 'YYYY-MM-DD' para datetime.date."""
        if data is None or data == "":
            return None

        if isinstance(data, date):
            return data

        try:
            return datetime.strptime(data, "%Y-%m-%d").date()
        except:
            return None

    def inserir(self, usuario_id, nickname, bio, pais, data_criacao):
        try:
            data_criacao = self._converter_data(data_criacao)

            sql = """
            INSERT INTO Perfil_Usuario (usuario_id_usuario, nickname, bio, pais, data_criacao)
            VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(sql, (usuario_id, nickname, bio, pais, data_criacao))
            self.conn.commit()
            print("Perfil criado com sucesso!")
        except Exception as e:
            print("Erro ao inserir perfil:", e)

    def atualizar(self, usuario_id_usuario, nickname=None, bio=None, pais=None, data_criacao=None):
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
                valores.append(self._converter_data(data_criacao))

            if not campos:
                print("Nenhum dado para atualizar!")
                return

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
        sql = "SELECT * FROM Perfil_Usuario"
        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()

            for r in resultados:
                if isinstance(r.get("data_criacao"), date):
                    r["data_criacao"] = r["data_criacao"].strftime("%Y/%m/%d")

            return resultados
        except Exception as e:
            print("Erro ao listar perfis:", e)
            return []


    def listar_perfis_com_usuario(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("""
                       SELECT p.usuario_id_usuario AS id_usuario,
                              p.nickname,
                              p.pais,
                              p.data_criacao,
                              u.email,
                              u.tipo_usuario
                       FROM perfil_usuario p
                                JOIN usuario u ON p.usuario_id_usuario = u.id_usuario;
                       """)
        return cursor.fetchall()