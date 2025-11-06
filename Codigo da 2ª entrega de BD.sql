DROP DATABASE IF EXISTS ProjetoBD;
CREATE DATABASE ProjetoBD;
USE ProjetoBD;

SET SQL_SAFE_UPDATES = 0; -- Utilizar Updates sem problemas

-- Criação das tabelas baseada no modelo desenvolvido na entrega anterior (atributos e relacionamentos);
-- Tabela: usuario
CREATE TABLE usuario (
    id_usuario INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(90) NOT NULL,
    senha VARCHAR(45) NOT NULL,
    tipo_usuario ENUM('comum', 'admin') NOT NULL DEFAULT 'comum',
    data_nascimento DATE NOT NULL,
    PRIMARY KEY (id_usuario),
    UNIQUE (email),
    UNIQUE (id_usuario)
);

-- Tabela: perfil_usuario
CREATE TABLE perfil_usuario (
    usuario_id_usuario INT NOT NULL,
    nickname VARCHAR(45) NOT NULL,
    bio VARCHAR(200) NULL,
    pais VARCHAR(45) NULL,
    data_criacao DATE NOT NULL,
    PRIMARY KEY (usuario_id_usuario),
    UNIQUE (nickname),
    CONSTRAINT fk_perfil_usuario__usuario
        FOREIGN KEY (usuario_id_usuario)
        REFERENCES usuario (id_usuario)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
);

-- Tabela: equipe
CREATE TABLE equipe (
    nome VARCHAR(45) NOT NULL,
    sigla VARCHAR(45) NOT NULL,
    pais VARCHAR(45) NOT NULL,
    PRIMARY KEY (nome),
    UNIQUE (sigla)
);

-- Tabela: pro_player
CREATE TABLE pro_player (
    id_pro_player INT NOT NULL AUTO_INCREMENT,
    nickname VARCHAR(45) NOT NULL,
    usuario_id_usuario INT NOT NULL,
    equipe_nome VARCHAR(45) NULL,
    PRIMARY KEY (id_pro_player),
    UNIQUE (id_pro_player),
    UNIQUE (usuario_id_usuario),
    UNIQUE (nickname),
    INDEX idx_pro_player__usuario (usuario_id_usuario),
    INDEX idx_pro_player__equipe (equipe_nome),
    CONSTRAINT fk_pro_player__usuario
        FOREIGN KEY (usuario_id_usuario)
        REFERENCES usuario (id_usuario)
        ON DELETE CASCADE
        ON UPDATE NO ACTION,
    CONSTRAINT fk_pro_player__equipe
        FOREIGN KEY (equipe_nome)
        REFERENCES equipe (nome)
        ON DELETE SET NULL
        ON UPDATE NO ACTION
);

-- Tabela: jogo
CREATE TABLE jogo (
    nome VARCHAR(45) NOT NULL,
    genero VARCHAR(45) NOT NULL,
    desenvolvedora VARCHAR(45) NOT NULL,
    PRIMARY KEY (nome)
);

-- Tabela: torneio
CREATE TABLE torneio (
    nome VARCHAR(45) NOT NULL,
    premiacao VARCHAR(45) NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    jogo_nome VARCHAR(45) NOT NULL,
    PRIMARY KEY (nome),
    UNIQUE (nome),
    INDEX idx_torneio__jogo (jogo_nome),
    CONSTRAINT fk_torneio__jogo
        FOREIGN KEY (jogo_nome)
        REFERENCES jogo (nome)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

-- Tabela: partida
CREATE TABLE partida (
    id_partida INT NOT NULL AUTO_INCREMENT,
    data DATE NOT NULL,
    fase VARCHAR(45) NOT NULL,
    torneio_nome VARCHAR(45) NOT NULL,
    PRIMARY KEY (id_partida),
    UNIQUE (id_partida),
    INDEX idx_partida__torneio (torneio_nome),
    CONSTRAINT fk_partida__torneio
        FOREIGN KEY (torneio_nome)
        REFERENCES torneio (nome)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

-- Tabela: participou
CREATE TABLE participou (
    partida_id_partida INT NOT NULL,
    ganhador VARCHAR(45) NOT NULL,
    equipe_nome VARCHAR(45) NOT NULL,
    PRIMARY KEY (partida_id_partida, equipe_nome),
    INDEX idx_participou__partida (partida_id_partida),
    INDEX idx_participou__equipe (equipe_nome),
    CONSTRAINT fk_participou__partida
        FOREIGN KEY (partida_id_partida)
        REFERENCES partida (id_partida)
        ON DELETE CASCADE
        ON UPDATE NO ACTION,
    CONSTRAINT fk_participou__equipe
        FOREIGN KEY (equipe_nome)
        REFERENCES equipe (nome)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
);

-- Tabela: inscricao
CREATE TABLE inscricao (
    equipe_nome VARCHAR(45) NOT NULL,
    torneio_nome VARCHAR(45) NOT NULL,
    data DATE NOT NULL,
    PRIMARY KEY (equipe_nome, torneio_nome),
    INDEX idx_inscricao__torneio (torneio_nome),
    INDEX idx_inscricao__equipe (equipe_nome),
    CONSTRAINT fk_inscricao__equipe
        FOREIGN KEY (equipe_nome)
        REFERENCES equipe (nome)
        ON DELETE CASCADE
        ON UPDATE NO ACTION,
    CONSTRAINT fk_inscricao__torneio
        FOREIGN KEY (torneio_nome)
        REFERENCES torneio (nome)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
);

-- Tabela: estatisticas
CREATE TABLE estatisticas (
    pro_player_id_pro_player INT NOT NULL,
    partida_id_partida INT NOT NULL,
    kda VARCHAR(45) NOT NULL,
    PRIMARY KEY (pro_player_id_pro_player, partida_id_partida),
    INDEX idx_estatisticas__partida (partida_id_partida),
    INDEX idx_estatisticas__pro_player (pro_player_id_pro_player),
    CONSTRAINT fk_estatisticas__pro_player
        FOREIGN KEY (pro_player_id_pro_player)
        REFERENCES pro_player (id_pro_player)
        ON DELETE CASCADE
        ON UPDATE NO ACTION,
    CONSTRAINT fk_estatisticas__partida
        FOREIGN KEY (partida_id_partida)
        REFERENCES partida (id_partida)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
);

-- Inserção de no mínimo 3 instâncias por tabela;
-- Inserções para usuario
INSERT INTO usuario (id_usuario, email, senha, tipo_usuario, data_nascimento) VALUES
(1, 'pedroph@email.com', 'senha123', 'comum', '1998-04-10'),
(2, 'danilocatita@email.com', 'abc456', 'admin', '1995-09-23'),
(3, 'pedroarmengol@email.com', 'qwe789', 'comum', '2000-12-02');
SELECT * FROM usuario;

-- Inserções para perfil_usuario
INSERT INTO perfil_usuario (usuario_id_usuario, nickname, bio, pais, data_criacao) VALUES 
(1, 'Seborreia', 'Apaixonado por jogos de FPS.', 'Brasil', '2023-06-15'), 
(2, 'Ratao', 'Administrador e criador da comunidade.', 'Portugal', '2022-11-04'), 
(3, 'Prematuro', 'Streamo jogos de terror.', 'Brasil', '2024-02-20');
SELECT * FROM perfil_usuario;

-- Inserções para equipe
INSERT INTO equipe (nome, sigla, pais) VALUES
('FURIA', 'FUR', 'Brasil'),
('G2 Esports', 'G2', 'Espanha'),
('T1', 'T1', 'Coreia do Sul');
SELECT * FROM equipe;

-- Inserções para pro_player
INSERT INTO pro_player (id_pro_player, nickname, usuario_id_usuario, equipe_nome) VALUES
(1, 'Seborreia', 1, 'FURIA'),
(2, 'Ratao', 2, 'G2 Esports'),
(3, 'Prematuro', 3, 'T1');
SELECT * FROM pro_player;

-- Inserções para jogo
INSERT INTO jogo (nome, genero, desenvolvedora) VALUES
('Counter-Strike 2', 'FPS', 'Valve'),
('Valorant', 'FPS', 'Riot Games'),
('League of Legends', 'MOBA', 'Riot Games');
SELECT * FROM jogo;

-- Inserções para torneio
INSERT INTO torneio (nome, premiacao, data_inicio, data_fim, jogo_nome) VALUES
('IEM Katowice 2024', 'US$250.000', '2024-02-01', '2024-02-11', 'Counter-Strike 2'),
('Valorant Champions 2024', 'US$1.000.000', '2024-08-06', '2024-08-24', 'Valorant'),
('Worlds 2024', 'US$2.000.000', '2024-10-01', '2024-10-31', 'League of Legends');
SELECT * FROM torneio;

-- Inserções para partida
INSERT INTO partida (id_partida, data, fase, torneio_nome) VALUES
(1, '2024-02-05', 'Quartas de Final', 'IEM Katowice 2024'),
(2, '2024-08-18', 'Semifinal', 'Valorant Champions 2024'),
(3, '2024-10-30', 'Final', 'Worlds 2024');
SELECT * FROM partida;

-- Inserções para participou
INSERT INTO participou (partida_id_partida, ganhador, equipe_nome) VALUES
(1, 'FURIA', 'FURIA'),
(3, 'T1', 'T1');
SELECT * FROM participou;

-- Inserções para inscricao
INSERT INTO inscricao (equipe_nome, torneio_nome, data) VALUES
('FURIA', 'IEM Katowice 2024', '2024-01-20'),
('G2 Esports', 'Valorant Champions 2024', '2024-07-15'),
('T1', 'Worlds 2024', '2024-09-10');
SELECT * FROM inscricao;

-- Inserções para estatisticas
INSERT INTO estatisticas (pro_player_id_pro_player, partida_id_partida, kda) VALUES
(1, 1, '20/10/5'),
(2, 2, '18/9/11'),
(3, 3, '12/1/14');
SELECT * FROM estatisticas;

-- Fazer 2 updates/deletes totais;
UPDATE perfil_usuario SET pais = 'Estados Unidos', bio = 'Jogador profissional de CS2 e criador de conteúdo.' WHERE nickname = 'Seborreia';
SELECT * FROM perfil_usuario;

DELETE FROM equipe WHERE nome = 'T1';
SELECT * FROM equipe;

-- Utilizar no mínimo 1 ALTER e no mínimo 1 DROP de sua escolha;
ALTER TABLE pro_player ADD titulos VARCHAR(1000);
UPDATE pro_player SET titulos = '3' WHERE id_pro_player = 1;
UPDATE pro_player SET titulos = '7' WHERE id_pro_player = 2;
UPDATE pro_player SET titulos = '4' WHERE id_pro_player = 3;
SELECT titulos FROM pro_player;
DROP TABLE estatisticas;

-- Criação de no mínimo 1 usuário de SGBD, o endereço pode ser de localhost e garanta privilégios (de sua escolha);
DROP USER IF EXISTS 'Admin1'@'localhost';
CREATE USER 'Admin1'@'localhost' IDENTIFIED BY 'abc456';
GRANT ALL PRIVILEGES ON ProjetoBD.* TO 'Admin1'@'localhost';
SELECT * FROM mysql.user;
SHOW GRANTS FOR 'Admin1'@'localhost';

-- Criação e utilização de 3 estruturas (Function, Procedures, Views ou Triggers).
DELIMITER $$
CREATE VIEW jogador_detalhado AS (
SELECT 
p.nickname AS 'Jogador',
pu.pais AS 'Nacionalidade',
e.nome AS 'Equipe',
i.torneio_nome AS 'Jogar'
FROM
pro_player p,
equipe e,
perfil_usuario pu,
inscricao i
WHERE 
p.equipe_nome = e.nome AND
pu.usuario_id_usuario = p.id_pro_player AND
i.equipe_nome = e.nome
)$$

CREATE TRIGGER avancar_fase
AFTER INSERT ON participou
FOR EACH ROW
BEGIN
    -- Cria uma nova partida de Final se a fase anterior foi Semifinal
    INSERT INTO partida (data, fase, torneio_nome)
    SELECT DATE_ADD(CURDATE(), INTERVAL 7 DAY),  -- curdate pega a data atual da partida, e o date add adiciona 7 dias a mais dessa data
           CASE 
               WHEN fase = 'Quartas de Final' THEN 'Semifinal'
               WHEN fase = 'Semifinal' THEN 'Final'
               ELSE NULL
           END,
           torneio_nome -- nome do torneio fixo 
    FROM partida
    WHERE id_partida = NEW.partida_id_partida -- limita criar a partida apenas para a selecionada
      AND fase IN ('Quartas de Final', 'Semifinal');
END$$

INSERT INTO participou (partida_id_partida, ganhador, equipe_nome) VALUES (2, 'G2 Esports', 'G2 Esports')$$

CREATE FUNCTION proxima_fase(fase_atual VARCHAR(45))
RETURNS VARCHAR(45)
DETERMINISTIC
BEGIN
    RETURN CASE
        WHEN fase_atual = 'Quartas de Final' THEN 'Semifinal'
        WHEN fase_atual = 'Semifinal' THEN 'Final'
        ELSE NULL
    END;
END$$

DELIMITER ;

SELECT proxima_fase('semifinal') AS Resultado;
DROP FUNCTION IF EXISTS proxima_fase;