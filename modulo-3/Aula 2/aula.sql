CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER
);

-- Adicione novas "fichas" (linhas) à sua gaveta.
INSERT INTO alunos(nome, idade) VALUES('Eduardo', 20);
INSERT INTO alunos(nome, idade) VALUES('Mônica', 21);

/*
Encontre informações com o comando mais importante!
Use WHERE para encontrar fichas com características específicas.
*/
SELECT * FROM alunos;
SELECT nome, idade FROM alunos;
SELECT * FROM alunos WHERE nome='Eduardo';

-- ltera informações de fichas que já existem.
UPDATE alunos SET idade = 23 WHERE nome = 'Eduardo';
-- Apaga fichas da sua gaveta.
DELETE FROM alunos WHERE nome = 'Carlos';
