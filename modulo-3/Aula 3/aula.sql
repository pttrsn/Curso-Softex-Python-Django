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
INSERT INTO professor(nome) VALUES('Francisco');
SELECT * FROM professor;

INSERT INTO aluno(nome, id_professor) VALUES('João', 1);
INSERT INTO aluno(nome, id_professor) VALUES('Maria', 1);
INSERT INTO aluno(nome, id_professor) VALUES('Fernando', 2);
SELECT * FROM aluno;
SELECT id AS Identificador, nome AS Nome FROM aluno;

SELECT aluno.nome as Aluno, professor.nome AS Professor
FROM aluno
INNER JOIN professor ON aluno.id_professor = professor.id;