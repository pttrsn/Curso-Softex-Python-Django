CREATE TABLE usuario (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE curso (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL
);

CREATE TABLE usuarios_cursos (
    id_usuario INTEGER NOT NULL,
    id_curso INTEGER NOT NULL,
    FOREIGN KEY(id_usuario) REFERENCES usuario(id),
    FOREIGN KEY(id_curso) REFERENCES curso(id)
);

INSERT INTO usuario(nome) VALUES('Carlos'), ('Francisco'), ('Maria');
INSERT INTO curso(titulo) VALUES ('Back-end'), ('Front-end');
INSERT INTO usuario_curso(id_usuario, id_curso) VALUES (1,1), (1,2), (2,1);

SELECT * FROM usuario;
SELECT * FROM curso;
SELECT * FROM usuario_curso;

SELECT usuario.nome, curso.titulo FROM usuario
INNER JOIN usuarios_cursos ON usuarios_cursos.id_usuario = usuario.id
INNER JOIN curso AS Curso ON usuarios_cursos.id_curso = curso.id;

SELECT count(*) FROM usuario;