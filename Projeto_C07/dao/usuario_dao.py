class UsuarioDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)  

    def inserir(self, email, senha, tipo_usuario, data_nascimento):
        sql = "INSERT INTO usuario (email, senha, tipo_usuario, data_nascimento) VALUES (%s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (email, senha, tipo_usuario, data_nascimento))
            self.conn.commit()
            print("Usuário inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir usuário:", e)

  

    def atualizar(self, id_usuario, email, senha, tipo_usuario, data_nascimento):
        sql = "UPDATE Usuario SET email=%s, senha=%s, tipo_usuario=%s, data_nascimento=%s WHERE id_usuario=%s"
        try:
            self.cursor.execute(sql, (email, senha, tipo_usuario, data_nascimento, id_usuario))
            self.conn.commit()
            print("Usuário atualizado!")
        except Exception as e:
            print("Erro ao atualizar usuário:", e)

    def deletar(self, id_usuario):
        sql = "DELETE FROM Usuario WHERE id_usuario=%s"
        try:
            self.cursor.execute(sql, (id_usuario,))
            self.conn.commit()
            print("Usuário deletado!")
        except Exception as e:
            print("Erro ao deletar usuário:", e)

    def listar(self):
        sql = "SELECT * FROM Usuario"
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print("Erro ao listar usuários:", e)
            return []
