# Plataforma de Torneios de eSports

---

## 1. Escopo do Projeto
Este projeto tem como objetivo modelar uma plataforma para gerenciamento de torneios de eSports.  
A aplicação contempla o cadastro de usuários, perfis públicos, jogadores profissionais (Pro Players), equipes, torneios e partidas.  

O modelo foi desenvolvido no **MySQL Workbench** e segue as instruções da disciplina, com presença mínima de **5 entidades** e relacionamentos dos tipos **1:1, 1:N e N:M**.

---

## 2. Entidades e Descrições
- **Usuario**: representa a conta do sistema, com email, senha e tipo de acesso (comum ou administrador).  
- **PerfilUsuario**: armazena as informações públicas do usuário, como nickname, bio e país. Cada usuário possui exatamente um perfil.  
- **ProPlayer**: representa jogadores profissionais que participam das partidas. Todo ProPlayer deve estar associado a um usuário, mas nem todo usuário precisa ser ProPlayer.  
- **Equipe**: times cadastrados para participar dos torneios, com nome, tag e país de origem.  
- **Jogo**: catálogo de jogos suportados pela plataforma (ex.: League of Legends, Valorant, CS:GO).  
- **Torneio**: campeonatos criados para um jogo específico, com nome, temporada e premiação.  
- **Partida**: confrontos realizados dentro de um torneio, com fase, rodada e data/hora.  
- **Inscricao**: tabela de junção entre Equipe e Torneio (N:M), indicando quais equipes se inscreveram em quais torneios.  
- **PartidaEquipe**: tabela de junção entre Partida e Equipe, indicando quais equipes jogaram em cada partida e o resultado.  
- **EstatisticaPartida**: tabela de junção entre Partida e ProPlayer, registrando estatísticas como kills, deaths e assists.  

---

## 3. Relacionamentos
- **Usuario – PerfilUsuario (1:1)**: cada usuário possui exatamente um perfil público.  
- **Usuario – ProPlayer (1:1 opcional)**: um ProPlayer deve ter vínculo com um usuário; um usuário pode ou não ser ProPlayer.  
- **Torneio – Partida (1:N)**: um torneio possui várias partidas; cada partida pertence a um torneio.  
- **Equipe – Torneio (N:M)**: representado pela tabela *Inscricao*. Uma equipe pode participar de vários torneios e um torneio pode ter várias equipes inscritas.  
- **Partida – Equipe (N:M)**: representado pela tabela *PartidaEquipe*. Cada partida envolve duas equipes.  
- **Partida – ProPlayer (N:M)**: representado pela tabela *EstatisticaPartida*. Cada jogador tem estatísticas associadas a cada partida.  
- **Jogo – Torneio (1:N)**: um jogo pode ter vários torneios; cada torneio pertence a um único jogo.  

---

## 4. Regras de Negócio
- Todo **ProPlayer** deve obrigatoriamente estar vinculado a um usuário.  
- Todo **Usuário** deve possuir um **PerfilUsuario** associado.  
- Uma **Partida** deve envolver **duas equipes distintas**.  
- Estatísticas de jogadores só podem existir se estiverem vinculadas a uma **Partida válida**.  
- A **Inscricao** de uma equipe em um torneio deve ter um status: *pendente, aprovado ou recusado*.  

---

## 5. Dupla
- **Antonio Feliciano da Silveira Neto** (@AntonioFSN2)  
- **Danilo Henrique Maia Silva** (@DaniloSilva31)  


