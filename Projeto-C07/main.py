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
            menu_pro_player(proplayer_dao)
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


# Menu Equipe (TA FUNCIONANDO)
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
            nome_atual = input("Nome da equipe a modificar: ")
            novo_nome = input("Novo Nome (vazio para não alterar): ") or None
            nova_sigla = input("Nova Sigla (vazio para não alterar): ") or None
            novo_pais = input("Novo País (vazio para não alterar): ") or None
            dao.atualizar(nome_atual, novo_nome, nova_sigla, novo_pais)


        elif opcao == "3":
            nome = input("Nome da equipe: ")
            dao.deletar(nome)


        elif opcao == "4":
            equipes = dao.listar()
            for e in equipes:
                print(e)

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

#FUNCIONANDO(porem tem q ver caso ele coloque o id errado ou algo assim)
def menu_pro_player(dao):
    while True:
        print("\n--- Menu Pro Player ---")
        print("1 - Inserir Pro Player")
        print("2 - Atualizar Pro Player")
        print("3 - Deletar Pro Player")
        print("4 - Listar Pro Players")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nickname = input("Nickname: ")
            usuario_id = int(input("ID do usuário associado: "))
            equipe_nome = input("Nome da equipe (vazio se não tiver): ") or None
            dao.inserir(nickname, usuario_id, equipe_nome)

        elif opcao == "2":
            idp = int(input("ID do Pro Player que deseja atualizar: "))
            print("Deixe vazio para não alterar:")
            nickname = input("Novo nickname: ") or None
            usuario_id = input("Novo ID de usuário: ")
            usuario_id = int(usuario_id) if usuario_id else None
            equipe_nome = input("Nova equipe: ") or None

            dao.atualizar(idp, nickname, usuario_id, equipe_nome)

        elif opcao == "3":
            idp = int(input("ID do Pro Player que deseja deletar: "))
            dao.deletar(idp)

        elif opcao == "4":
            jogadores = dao.listar()
            print("\n--- Lista de Pro Players ---")
            for j in jogadores:
                print(f"ID: {j['id_pro_player']} | Nickname: {j['nickname']} | Usuario ID: {j['usuario_id_usuario']} | Equipe: {j['equipe_nome']}")

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
