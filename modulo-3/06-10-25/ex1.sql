CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);

CREATE TABLE postagens (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    postagem TEXT NOT NULL,
    id_autor INTEGER
);

INSERT INTO usuarios(nome, sobrenome, email, senha) VALUES('Eduardo', 'Pereira', 'eduardo.pereira@email.com', 'eduardo.per@2025');
INSERT INTO usuarios(nome, sobrenome, email, senha) VALUES('Mônica', 'Alves', 'monica.alves@email.com', 'monica.alv@2025');
INSERT INTO usuarios(nome, sobrenome, email, senha) VALUES('Pedro', 'Souza', 'pedro.souza@email.com', 'pedro.sou@2025');
INSERT INTO usuarios(nome, sobrenome, email, senha) VALUES('Carlos', 'Maia', 'carlos.maia@email.com', 'carlos.mai@2025');
INSERT INTO usuarios(nome, sobrenome, email, senha) VALUES('Ryan', 'Ribeiro', 'ryan.ribeiro@email.com', 'ryan.rib@2025');


INSERT INTO postagens(titulo, postagem, id_autor) VALUES('Post 1', 'Lorem ipsum', 0001);
INSERT INTO postagens(titulo, postagem, id_autor) VALUES('Post 2', 'Lorem ipsum', 0002);
INSERT INTO postagens(titulo, postagem, id_autor) VALUES('Post 3', 'Lorem ipsum', 0003);
INSERT INTO postagens(titulo, postagem, id_autor) VALUES('Post 4', 'Lorem ipsum', 0004);
INSERT INTO postagens(titulo, postagem, id_autor) VALUES('Post 5', 'Lorem ipsum', 0005);


SELECT * FROM usuarios;
SELECT * FROM postagens;