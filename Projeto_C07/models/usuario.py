class Usuario:
    def __init__(self, id_usuario=None, email=None, senha=None, tipo_usuario='comum', data_nascimento=None):
        self.id_usuario = id_usuario
        self.email = email
        self.senha = senha
        self.tipo_usuario = tipo_usuario
        self.data_nascimento = data_nascimento
