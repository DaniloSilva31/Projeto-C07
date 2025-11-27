from datetime import datetime, date

class UsuarioDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)


    def _converter_data(self, data):
        """Converte 'YYYY-MM-DD' em datetime.date"""
        if data is None or data == "":
            return None

        if isinstance(data, date):
            return data

        try:
            return datetime.strptime(data, "%Y-%m-%d").date()
        except:
            return None

    def inserir(self, email, senha, tipo_usuario, data_nascimento):
        try:
            data_nascimento = self._converter_data(data_nascimento)

            sql = """
                  INSERT INTO usuario (email, senha, tipo_usuario, data_nascimento)
                  VALUES (%s, %s, %s, %s) \
                  """
            self.cursor.execute(sql, (email, senha, tipo_usuario, data_nascimento))
            self.conn.commit()
            print("Usuário inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir usuário:", e)

    def atualizar(self, id_usuario, email=None, senha=None, tipo_usuario=None, data_nascimento=None):
        try:
            campos = []
            valores = []

            if email is not None:
                campos.append("email=%s")
                valores.append(email)

            if senha is not None:
                campos.append("senha=%s")
                valores.append(senha)

            if tipo_usuario is not None:
                campos.append("tipo_usuario=%s")
                valores.append(tipo_usuario)

            if data_nascimento is not None:
                campos.append("data_nascimento=%s")
                valores.append(self._converter_data(data_nascimento))

            if not campos:
                print("Nenhum dado para atualizar!")
                return

            valores.append(id_usuario)

            sql = "UPDATE usuario SET " + ", ".join(campos) + " WHERE id_usuario=%s"
            self.cursor.execute(sql, valores)
            self.conn.commit()
            print("Usuário atualizado!")

        except Exception as e:
            print("Erro ao atualizar usuário:", e)

    def deletar(self, id_usuario):
        try:
            sql = "DELETE FROM usuario WHERE id_usuario=%s"
            self.cursor.execute(sql, (id_usuario,))
            self.conn.commit()
            print("Usuário deletado!")
        except Exception as e:
            print("Erro ao deletar usuário:", e)

    def listar(self):
        try:
            sql = "SELECT * FROM usuario"
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()

            # Formata datas
            for r in resultados:
                if isinstance(r.get("data_nascimento"), date):
                    r["data_nascimento"] = r["data_nascimento"].strftime("%Y/%m/%d")

            return resultados

        except Exception as e:
            print("Erro ao listar usuários:", e)
            return[]
        
    def listar_usuario_perfil_e_proplayer(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT u.id_usuario, u.email, u.tipo_usuario, p.nickname AS perfil, pr.nickname AS proplayer
            FROM usuario u
            LEFT JOIN perfil_usuario p ON p.usuario_id_usuario = u.id_usuario
            LEFT JOIN pro_player pr ON pr.usuario_id_usuario = u.id_usuario;
        """)
        return cursor.fetchall()    
        
        