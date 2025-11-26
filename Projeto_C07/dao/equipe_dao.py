class EquipeDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)

    def inserir(self, nome, sigla, pais):
        try:
            sql = "INSERT INTO Equipe (nome, sigla, pais) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (nome, sigla, pais))
            self.conn.commit()
            print("Equipe inserida com sucesso!")
        except Exception as e:
            print("Erro ao inserir equipe:", e)

    def atualizar(self, nome=None, sigla=None, pais=None):
        try:
            campos = []
            valores = []

            if nome is not None:
                campos.append("nome=%s")
                valores.append(nome)
            if sigla is not None:
                campos.append("sigla=%s")
                valores.append(sigla)
            if pais is not None:
                campos.append("pais_origem=%s")
                valores.append(pais)

            sql = "UPDATE Equipe SET " + ", ".join(campos) + " WHERE nome=%s"
            self.cursor.execute(sql, valores)
            self.conn.commit()
            print("Equipe atualizada!")
        except Exception as e:
            print("Erro ao atualizar equipe:", e)

    def deletar(self, id_equipe):
        try:
            sql = "DELETE FROM Equipe WHERE id=%s"
            self.cursor.execute(sql, (id_equipe,))
            self.conn.commit()
            print("Equipe deletada!")
        except Exception as e:
            print("Erro ao deletar equipe:", e)

    def listar_todos(self):
        try:
            self.cursor.execute("SELECT * FROM Equipe")
            return self.cursor.fetchall()
        except Exception as e:
            print("Erro ao listar equipes:", e)
            return []

    def buscar_por_id(self, id_equipe):
        try:
            sql = "SELECT * FROM Equipe WHERE id=%s"
            self.cursor.execute(sql, (id_equipe,))
            return self.cursor.fetchone()
        except Exception as e:
            print("Erro ao buscar equipe:", e)
            return None
