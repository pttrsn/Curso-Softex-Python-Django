/*
Exercício 1: Relacionamento Um para Muitos (1:N) 
 
Cenário: Uma biblioteca precisa gerenciar livros e autores. 
Passo 1: Inserção de Dados 
●  Tabela autores: 
○  Atributos: id_autor, nome, nacionalidade. 
○  Pedidos de Inserção: 
■  Insira 2 autores. 
●  Tabela livros: 
○  Atributos: id_livro, titulo, ano_publicacao, id_autor (chave estrangeira). 
○  Pedidos de Inserção: 
■  Insira 3 livros, associando-os aos autores que você criou. 
Passo 2: Pedidos de Consulta 
1.  Consulta sem JOIN: Selecione o título de todos os livros e o ano de publicação. 
2.  Consulta com JOIN e filtro: Mostre o título de cada livro e o nome do seu autor. 
3.  Consulta com JOIN e filtro WHERE: Mostre os títulos dos livros e os nomes dos 
autores com a nacionalidade 'Britânica'. 
4.  Consulta com COUNT: Conte quantos livros cada autor escreveu.
*/

CREATE TABLE autores (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT NOT NULL
);

CREATE TABLE livros(
    id_livro INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    publicacao TEXT NOT NULL,
    id_autor INTEGER NOT NULL,
    FOREIGN KEY (id_autor) REFERENCES autores(id)
);

INSERT INTO autores(nome, nacionalidade) VALUES ('Machado de Assis', 'Brasil'), ('Clarice Lispector', 'Brasil');
INSERT INTO livros(titulo, publicacao, id_autor) VALUES ('Dom Casmurro', '1899', 1), ('Memórias Póstumas de Brás Cubas', '1881', 1), ('A Hora da Estrela', '1977', 2);

SELECT * FROM autores;
SELECT titulo, publicacao FROM livros;

SELECT livros.titulo AS Obra, autores.nome AS Autor 
FROM livros
INNER JOIN autores ON livros.id_autor = autores.id;
