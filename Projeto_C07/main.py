from models.usuario import Usuario
from models.perfil import PerfilUsuario
from models.equipe import Equipe
from models.proplayer import ProPlayer
from models.torneio import Torneio

from dao.usuario_dao import UsuarioDAO
from dao.perfil_dao import PerfilUsuarioDAO
from dao.equipe_dao import EquipeDAO
from dao.proplayer_dao import ProPlayerDAO
from dao.torneio_dao import TorneioDAO

import mysql.connector

# Conexão
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="ProjetoBD"
)

# Instanciando DAOs
usuario_dao = UsuarioDAO(conn)
perfil_dao = PerfilUsuarioDAO(conn)
equipe_dao = EquipeDAO(conn)
proplayer_dao = ProPlayerDAO(conn)
torneio_dao = TorneioDAO(conn)


# Função principal
def main():
    menu_principal(usuario_dao, perfil_dao, equipe_dao, proplayer_dao, torneio_dao)


# Menu principal
def menu_principal(usuario_dao, perfil_dao, equipe_dao, proplayer_dao, torneio_dao):
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Gerenciar Usuários")
        print("2 - Gerenciar Perfis")
        print("3 - Gerenciar Equipes")
        print("4 - Gerenciar ProPlayers")
        print("5 - Gerenciar Torneios")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_usuario(usuario_dao)
        elif opcao == "2":
            menu_perfil(perfil_dao)
        elif opcao == "3":
            menu_equipe(equipe_dao)
        elif opcao == "4":
            menu_proplayer(proplayer_dao)
        elif opcao == "5":
            menu_torneio(torneio_dao)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


# Menu Usuário (ESTA FUNCIONANDO TUDO AQUI)
def menu_usuario(dao):
    while True:
        print("\n--- Menu Usuário ---")
        print("1 - Inserir Usuário")
        print("2 - Atualizar Usuário")
        print("3 - Deletar Usuário")
        print("4 - Listar todos os Usuários")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            email = input("Email: ")
            senha = input("Senha: ")
            tipo_usuario = input("Tipo de usuario (comum/admin): ") or 'comum'
            data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
            dao.inserir(email, senha, tipo_usuario, data_nascimento)

        elif opcao == "2":
            id_usuario = int(input("ID do Usuário: "))
            email = input("Novo Email: ")
            senha = input("Nova Senha: ")
            tipo_usuario = input("Novo Tipo de usuario: ")
            data_nascimento = input("Nova data de nascimento (YYYY-MM-DD): ")

            dao.atualizar(id_usuario, email, senha, tipo_usuario,data_nascimento)

        elif opcao == "3":
            id_usuario = int(input("ID do Usuário: "))
            dao.deletar(id_usuario)

        elif opcao == "4":
            usuarios = dao.listar()
            for u in usuarios:
                print(u)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# Menu Perfil
def menu_perfil(dao):
    while True:
        print("\n--- Menu Perfil ---")
        print("1 - Inserir Perfil")
        print("2 - Atualizar Perfil")
        print("3 - Deletar Perfil")
        print("4 - Listar Perfis")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario_id = int(input("ID do Usuário: "))
            nickname = input("Nickname: ")
            bio = input("Bio: ")
            pais = input("País: ")
            dao.inserir(usuario_id, nickname, bio, pais)

        elif opcao == "2":
            id_perfil = int(input("ID do Perfil: "))
            nickname = input("Novo Nickname (deixe vazio para não alterar): ") or None
            bio = input("Nova Bio (deixe vazio para não alterar): ") or None
            pais = input("Novo País (deixe vazio para não alterar): ") or None
            dao.atualizar(id_perfil, nickname, bio, pais)

        elif opcao == "3":
            id_perfil = int(input("ID do Perfil: "))
            dao.deletar(id_perfil)

        elif opcao == "4":
            perfis = dao.listar()
            for p in perfis:
                print(p)

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# Menu Equipe
def menu_equipe(dao):
    while True:
        print("\n--- Menu Equipe ---")
        print("1 - Inserir Equipe")
        print("2 - Atualizar Equipe")
        print("3 - Deletar Equipe")
        print("4 - Listar Equipes")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            sigla = input("Sigla: ")
            pais = input("País: ")
            dao.inserir(nome, sigla, pais)

        elif opcao == "2":
            id_equipe = int(input("ID da Equipe: "))
            nome = input("Novo Nome (vazio para não alterar): ") or None
            sigla = input("Nova sigla (vazio para não alterar): ") or None
            pais = input("Novo País (vazio para não alterar): ") or None
            dao.atualizar(id_equipe, nome, sigla, pais)

        elif opcao == "3":
            id_equipe = int(input("ID da Equipe: "))
            dao.deletar(id_equipe)

        elif opcao == "4":
            equipes = dao.listar()
            for e in equipes:
                print(e)

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# Menu ProPlayer
def menu_proplayer(dao):
    while True:
        print("\n--- Menu ProPlayer ---")
        print("1 - Inserir ProPlayer")
        print("2 - Atualizar ProPlayer")
        print("3 - Deletar ProPlayer")
        print("4 - Listar ProPlayers")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nickname = input("Nickname: ")
            usuario_id = int(input("ID do Usuário: "))
            equipe_nome = input("Nome da Equipe (ou vazio): ") or None
            dao.inserir(nickname, usuario_id, equipe_nome)
            #AQUI ESTA FUNCIONANDO 

        elif opcao == "2":
            id_player = int(input("ID do ProPlayer: "))
            nickname = input("Novo Nickname: ")
            usuario_id = int(input("Novo ID do Usuário: "))
            equipe_nome = input("Novo Nome da Equipe (ou vazio): ") or None
            dao.atualizar(id_player, nickname, usuario_id, equipe_nome)

        elif opcao == "3":
            id_player = int(input("ID do ProPlayer: "))
            dao.deletar(id_player)

        elif opcao == "4":
            players = dao.listar_todos()
            for p in players:
                print(p)

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# Menu Torneio
def menu_torneio(dao):
    while True:
        print("\n--- Menu Torneio ---")
        print("1 - Inserir Torneio")
        print("2 - Atualizar Torneio")
        print("3 - Deletar Torneio")
        print("4 - Listar Torneios")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            jogo_id = int(input("ID do Jogo: "))
            data_inicio = input("Data de início (YYYY-MM-DD): ")
            dao.inserir(nome, jogo_id, data_inicio)

        elif opcao == "2":
            id_torneio = int(input("ID do Torneio: "))
            nome = input("Novo Nome (vazio para não alterar): ") or None
            jogo_id = input("Novo ID do Jogo (vazio para não alterar): ") or None
            data_inicio = input("Nova Data (vazio para não alterar): ") or None
            dao.atualizar(id_torneio, nome, jogo_id, data_inicio)

        elif opcao == "3":
            id_torneio = int(input("ID do Torneio: "))
            dao.deletar(id_torneio)

        elif opcao == "4":
            torneios = dao.listar()
            for t in torneios:
                print(t)

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
