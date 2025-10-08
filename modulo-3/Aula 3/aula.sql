CREATE TABLE professor (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE aluno (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    id_professor INTEGER,
    FOREIGN KEY (id_professor) REFERENCES professor(id)
);

INSERT INTO professor(nome) VALUES('Carlos');
SELECT * FROM professor;

INSERT INTO aluno(nome, id_professor) VALUES('João', 1);
INSERT INTO aluno(nome, id_professor) VALUES('Maria', 1);
SELECT * FROM aluno;

