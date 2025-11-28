CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_compra DATETIME NOT NULL DEFAULT (datetime('now')),
    total REAL NOT NULL,
    id_cliente INTEGER NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS itens_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pedido INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (id_produto) REFERENCES produtos(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

INSERT INTO clientes (nome, email) VALUES
  ('João',  'joao@example.com'),
  ('Maria', 'maria@example.com'),
  ('Ana',   'ana@example.com');

INSERT INTO produtos (nome, preco, estoque) VALUES
  ('Teclado', 120.00, 50),
  ('Mouse',    80.00, 100),
  ('Monitor', 950.90, 20);

INSERT INTO pedidos (data_compra, total, id_cliente)
VALUES (datetime('now'), 0.0, (SELECT id FROM clientes WHERE nome = 'Maria'));

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade)
VALUES (
    (SELECT id FROM pedidos WHERE id_cliente = (SELECT id FROM clientes WHERE nome = 'Maria') ORDER BY id DESC LIMIT 1),
    (SELECT id FROM produtos WHERE nome = 'Teclado'),
    1
);

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade)
VALUES (
    (SELECT id FROM pedidos WHERE id_cliente = (SELECT id FROM clientes WHERE nome = 'Maria') ORDER BY id DESC LIMIT 1),
    (SELECT id FROM produtos WHERE nome = 'Mouse'),
    2
);

UPDATE pedidos
SET total = (
    SELECT SUM(p.preco * ip.quantidade)
    FROM itens_pedido ip
    JOIN produtos p ON p.id = ip.id_produto
    WHERE ip.id_pedido = (
        SELECT id FROM pedidos WHERE id_cliente = (SELECT id FROM clientes WHERE nome = 'Maria') ORDER BY id DESC LIMIT 1
    )
)
WHERE id = (
    SELECT id FROM pedidos WHERE id_cliente = (SELECT id FROM clientes WHERE nome = 'Maria') ORDER BY id DESC LIMIT 1
);

SELECT nome, preco
FROM produtos
WHERE preco > 100.00;

SELECT c.nome AS nome_cliente, p.id AS id_pedido, p.data_compra
FROM pedidos p
JOIN clientes c ON c.id = p.id_cliente
WHERE c.nome = 'Maria';

UPDATE produtos
SET preco = ROUND(preco * 1.10, 2)
WHERE nome = 'Mouse';

UPDATE produtos
SET estoque = estoque - 2
WHERE nome = 'Mouse';

DELETE FROM clientes
WHERE nome = 'João';

DELETE FROM itens_pedido
WHERE id_pedido = (
    SELECT p.id
    FROM pedidos p
    WHERE p.id_cliente = (SELECT id FROM clientes WHERE nome = 'Maria')
    ORDER BY p.id DESC
    LIMIT 1
)
AND id_produto = (SELECT id FROM produtos WHERE nome = 'Teclado');

UPDATE pedidos
SET total = (
    SELECT COALESCE(SUM(p.preco * ip.quantidade), 0)
    FROM itens_pedido ip
    JOIN produtos p ON p.id = ip.id_produto
    WHERE ip.id_pedido = (
        SELECT id FROM pedidos WHERE id_cliente = (SELECT id FROM clientes WHERE nome = 'Maria') ORDER BY id DESC LIMIT 1
    )
)
WHERE id = (
    SELECT id FROM pedidos WHERE id_cliente = (SELECT id FROM clientes WHERE nome = 'Maria') ORDER BY id DESC LIMIT 1
);