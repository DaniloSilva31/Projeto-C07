class EquipeDAO:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)

    def inserir(self, nome, sigla, pais):
        try:
            sql = "INSERT INTO equipe (nome, sigla, pais) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (nome, sigla, pais))
            self.conn.commit()
            print("Equipe inserida com sucesso!")
        except Exception as e:
            print("Erro ao inserir equipe:", e)

    def atualizar(self, nome_atual, novo_nome=None, nova_sigla=None, novo_pais=None):
        try:
            campos = []
            valores = []

            if novo_nome:
                campos.append("nome=%s")
                valores.append(novo_nome)
            if nova_sigla:
                campos.append("sigla=%s")
                valores.append(nova_sigla)
            if novo_pais:
                campos.append("pais=%s") 
                valores.append(novo_pais)

            if not campos:
                print("Nenhuma atualização feita.")
                return

            sql = "UPDATE equipe SET " + ", ".join(campos) + " WHERE nome=%s"
            valores.append(nome_atual)

            self.cursor.execute(sql, valores)
            self.conn.commit()
            print("Equipe atualizada com sucesso!")
        except Exception as e:
            print("Erro ao atualizar equipe:", e)

    def deletar(self, nome):
        try:
            sql = "DELETE FROM equipe WHERE nome=%s"
            self.cursor.execute(sql, (nome,))
            self.conn.commit()
            print("Equipe deletada com sucesso!")
        except Exception as e:
            print("Erro ao deletar equipe:", e)

    def listar(self):
        try:
            self.cursor.execute("SELECT * FROM equipe")
            return self.cursor.fetchall()
        except Exception as e:
            print("Erro ao listar equipes:", e)
            return []

    def buscar_por_nome(self, nome):
        try:
            sql = "SELECT * FROM equipe WHERE nome=%s"
            self.cursor.execute(sql, (nome,))
            return self.cursor.fetchone()
        except Exception as e:
            print("Erro ao buscar equipe:", e)
            return None
        
    def listar_equipe_com_proplayers(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT e.nome AS equipe, e.sigla, e.pais, pr.id_pro_player, pr.nickname AS proplayer
            FROM equipe e
            LEFT JOIN pro_player pr ON pr.equipe_nome = e.nome;
        """)
        return cursor.fetchall()
