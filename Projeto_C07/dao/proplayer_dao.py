class ProPlayerDAO:
    def __init__(self, conn):
        self.conn = conn

    def inserir(self, nickname, usuario_id_usuario, equipe_nome=None, titulos=None):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO pro_player (nickname, usuario_id_usuario, equipe_nome, titulos) VALUES (%s, %s, %s, %s)",
            (nickname, usuario_id_usuario, equipe_nome, titulos)
        )
        self.conn.commit()

    def atualizar(self, id_pro_player, nickname=None, usuario_id_usuario=None, equipe_nome=None, titulos=None):
        cursor = self.conn.cursor()
        query = "UPDATE pro_player SET "
        campos = []
        valores = []

        if nickname is not None:
            campos.append("nickname = %s")
            valores.append(nickname)
        if usuario_id_usuario is not None:
            campos.append("usuario_id_usuario = %s")
            valores.append(usuario_id_usuario)
        if equipe_nome is not None:
            campos.append("equipe_nome = %s")
            valores.append(equipe_nome)
        if titulos is not None:
            campos.append("titulos = %s")
            valores.append(titulos)

        query += ", ".join(campos)
        query += " WHERE id_pro_player = %s"
        valores.append(id_pro_player)

        cursor.execute(query, tuple(valores))
        self.conn.commit()

    def deletar(self, id_pro_player):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM pro_player WHERE id_pro_player = %s", (id_pro_player,))
        self.conn.commit()

    def listar(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pro_player")
        return cursor.fetchall()

    def listar_pro_players_com_equipe(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.id_pro_player, p.nickname, p.titulos, u.email AS usuario_email, u.tipo_usuario, e.nome AS equipe_nome, e.pais AS equipe_pais
            FROM pro_player p
            JOIN usuario u ON p.usuario_id_usuario = u.id_usuario
            LEFT JOIN equipe e ON p.equipe_nome = e.nome
        """)
        return cursor.fetchall()

    def listar_perfil_proplayer_e_equipe(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                p.id_pro_player,
                p.nickname AS nickname_proplayer,
                pf.nickname AS nickname_perfil,
                pf.bio,
                pf.pais,
                e.nome AS equipe,
                e.sigla,
                e.pais AS pais_equipe
            FROM pro_player p
            JOIN perfil_usuario pf ON p.usuario_id_usuario = pf.usuario_id_usuario
            LEFT JOIN equipe e ON p.equipe_nome = e.nome;
        """)
        return cursor.fetchall()
