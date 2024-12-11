-- Active: 1733917816560@@127.0.0.1@3306@teste_php

SELECT * FROM usuario;

TRUNCATE Table usuario;

INSERT INTO usuario(nome, senha, setor) VALUES ('Henrique', '123', 'comum');
INSERT INTO usuario(nome, senha, setor) VALUES ('Adm', 'Adm', 'adm');

DROP Table usuario ;

ALTER TABLE USUARIO ADD COLUMN setor VARCHAR(10);

CREATE TABLE usuario (
    id_cliente int AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30),
    lastname VARCHAR(30),
    sexo VARCHAR(30),
    fone VARCHAR(15),
    address VARCHAR(40),
    senha VARCHAR(30),
    email VARCHAR(50),
    setor VARCHAR(20) DEFAULT 'comum');

CREATE TABLE produtos(
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30),
    descricao VARCHAR(50),
    preco VARCHAR(20)
);
 
INSERT INTO produtos VALUES
(null, "Teclado", "Mouse", "100,00"),
(null, "Caixa", "Som", "30,00"),
(null, "Fone", "Ouvido", "44,00");
 
SELECT * FROM produtos;
 
 