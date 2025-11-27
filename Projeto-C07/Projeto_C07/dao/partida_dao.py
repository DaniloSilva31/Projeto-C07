# models/partida.py
class Partida:
    def __init__(self, id_partida=None, data=None, fase=None, torneio_nome=None):
        self.id_partida = id_partida
        self.data = data
        self.fase = fase
        self.torneio_nome = torneio_nome
