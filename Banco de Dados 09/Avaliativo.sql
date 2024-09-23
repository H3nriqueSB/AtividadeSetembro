CREATE DATABASE avaliativo;
USE avaliativo;

CREATE TABLE estado (
    id_estado INT PRIMARY KEY AUTO_INCREMENT,
    nome_estado VARCHAR(100)
);

CREATE TABLE cidade (
    id_cidade INT PRIMARY KEY AUTO_INCREMENT,
    nome_cidade VARCHAR(255),
    id_estado INT NOT NULL,
    FOREIGN KEY (id_estado) REFERENCES estado(id_estado)
);

CREATE TABLE genero (
    id_genero INT PRIMARY KEY AUTO_INCREMENT,
    nome_genero VARCHAR(20)
);

CREATE TABLE raca (
    id_raca INT PRIMARY KEY AUTO_INCREMENT,
    nome_raca VARCHAR(50)
);

CREATE TABLE estadocivil (
    id_estadocivil INT PRIMARY KEY AUTO_INCREMENT,
    nome_estadocivil VARCHAR(50)
);

CREATE TABLE religiao (
    id_religiao INT PRIMARY KEY AUTO_INCREMENT,
    nome_religiao VARCHAR(50)
);

CREATE TABLE agencia (
    id_agencia INT PRIMARY KEY AUTO_INCREMENT,
    nome_agencia VARCHAR(255),
    numagencia VARCHAR(3) UNIQUE,
    id_estado INT NOT NULL,
    FOREIGN KEY (id_estado) REFERENCES estado(id_estado)
);

CREATE TABLE endereco (
    id_endereco INT PRIMARY KEY AUTO_INCREMENT,
    rua VARCHAR(255),
    bairro VARCHAR(255),
    cep VARCHAR(11),
    numcasa VARCHAR(4),
    id_cidade INT NOT NULL,
    FOREIGN KEY (id_cidade) REFERENCES cidade(id_cidade)
);

CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    cpf VARCHAR(11) UNIQUE,
    rg VARCHAR(9) UNIQUE,
    datanasci DATE,
    fone VARCHAR(11),
    saldo FLOAT,
    id_endereco INT,
    id_genero INT,
    id_raca INT,
    id_religiao INT,
    id_estadocivil INT,
    id_agencia INT,
    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco),
    FOREIGN KEY (id_genero) REFERENCES genero(id_genero),
    FOREIGN KEY (id_raca) REFERENCES raca(id_raca),
    FOREIGN KEY (id_religiao) REFERENCES religiao(id_religiao),
    FOREIGN KEY (id_estadocivil) REFERENCES estadocivil(id_estadocivil),
    FOREIGN KEY (id_agencia) REFERENCES agencia(id_agencia)
);

CREATE TABLE saque (
    id_operacao INT PRIMARY KEY AUTO_INCREMENT,
    id_agencia INT,
    id_cliente INT,
    valor_saque FLOAT,
    FOREIGN KEY (id_agencia) REFERENCES agencia(id_agencia),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE deposito (
    id_operacao INT PRIMARY KEY AUTO_INCREMENT,
    id_agencia INT,
    id_cliente INT,
    valor_deposito FLOAT,
    FOREIGN KEY (id_agencia) REFERENCES agencia(id_agencia),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

INSERT INTO estado (nome_estado) VALUES 
('Acre'), ('Alagoas'), ('Amapá'), ('Amazonas'), 
('Bahia'), ('Ceará'), ('Distrito Federal'), ('Espírito Santo'), 
('Goiás'), ('Maranhão'), ('Mato Grosso'), ('Mato Grosso do Sul'), 
('Minas Gerais'), ('Pará'), ('Paraíba'), ('Paraná'), 
('Pernambuco'), ('Piauí'), ('Rio de Janeiro'), ('Rio Grande do Norte'), 
('Rio Grande do Sul'), ('Rondônia'), ('Roraima'), ('Santa Catarina'), 
('São Paulo'), ('Sergipe'), ('Tocantins');

INSERT INTO cidade (nome_cidade, id_estado) VALUES 
('Rio Branco', 1), ('Cruzeiro do Sul', 1), ('Sena Madureira', 1),
('Maceió', 2), ('Arapiraca', 2), ('Palmeira dos Índios', 2),
('Macapá', 3), ('Santana', 3), ('Laranjal do Jari', 3),
('Manaus', 4), ('Parintins', 4), ('Itacoatiara', 4),
('Salvador', 5), ('Feira de Santana', 5), ('Vitória da Conquista', 5),
('Fortaleza', 6), ('Caucaia', 6), ('Juazeiro do Norte', 6),
('Brasília', 7), ('Gama', 7), ('Taguatinga', 7),
('Vitória', 8), ('Vila Velha', 8), ('Cariacica', 8),
('Goiânia', 9), ('Aparecida de Goiânia', 9), ('Anápolis', 9),
('São Luís', 10), ('Imperatriz', 10), ('Caxias', 10),
('Cuiabá', 11), ('Várzea Grande', 11), ('Rondonópolis', 11),
('Campo Grande', 12), ('Dourados', 12), ('Três Lagoas', 12),
('Belo Horizonte', 13), ('Uberlândia', 13), ('Contagem', 13),
('Belém', 14), ('Ananindeua', 14), ('Santana', 14),
('João Pessoa', 15), ('Campina Grande', 15), ('Patos', 15),
('Curitiba', 16), ('Londrina', 16), ('Ponta Grossa', 16),
('Recife', 17), ('Olinda', 17), ('Jaboatão dos Guararapes', 17),
('Teresina', 18), ('Parnaíba', 18), ('Picos', 18),
('Rio de Janeiro', 19), ('Niterói', 19), ('Duque de Caxias', 19),
('Natal', 20), ('Mossoró', 20), ('Caicó', 20),
('Porto Alegre', 21), ('Canoas', 21), ('Pelotas', 21),
('Porto Velho', 22), ('Ji-Paraná', 22), ('Cacoal', 22),
('Boa Vista', 23), ('Rorainópolis', 23), ('Caracaraí', 23),
('Florianópolis', 24), ('Joinville', 24), ('Blumenau', 24),
('São Paulo', 25), ('Campinas', 25), ('São Bernardo do Campo', 25),
('Aracaju', 26), ('Lagarto', 26), ('Itabaiana', 26),
('Palmas', 27), ('Araguaína', 27), ('Gurupi', 27);

INSERT INTO genero (nome_genero) VALUES 
('Masculino'), 
('Feminino'), 
('Outro');

INSERT INTO raca (nome_raca) VALUES 
('Branco'), 
('Pardo'), 
('Negro');

INSERT INTO estadocivil (nome_estadocivil) VALUES 
('Solteiro'), 
('Casado'), 
('Divorciado');

INSERT INTO religiao (nome_religiao) VALUES 
('Católica'), 
('Evangélica'), 
('Ateia');

INSERT INTO agencia (nome_agencia, numagencia, id_estado) VALUES 
('Agência Central', '001', 25), 
('Agência Sul', '002', 19);

INSERT INTO endereco (rua, bairro, cep, numcasa, id_cidade) VALUES 
('Rua A', 'Centro', '01000-000', '1', 1), 
('Rua B', 'Copacabana', '22000-000', '2', 2),
('Rua C', 'Savassi', '30100-000', '3', 3);

INSERT INTO cliente (nome, cpf, rg, datanasci, fone, saldo, id_endereco, id_genero, id_raca, id_religiao, id_estadocivil, id_agencia) VALUES 
('João Silva', '12345678901', '123456789', '1980-01-01', '11999999999', 1000.00, 1, 1, 1, 1, 1, 1), 
('Maria Oliveira', '98765432100', '987654321', '1990-05-15', '21888888888', 2000.00, 2, 2, 2, 2, 2, 2);

INSERT INTO saque (id_agencia, id_cliente, valor_saque) VALUES 
(1, 1, 100.00), 
(2, 2, 200.00);

INSERT INTO deposito (id_agencia, id_cliente, valor_deposito) VALUES 
(1, 1, 300.00), 
(2, 2, 150.00);

DELIMITER //
CREATE TRIGGER antes_saque
AFTER INSERT ON saque
FOR EACH ROW
BEGIN
    DECLARE saldo_atual FLOAT;

    SELECT saldo INTO saldo_atual
    FROM cliente
    WHERE id_cliente = NEW.id_cliente;

    IF saldo_atual < NEW.valor_saque THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Saldo insuficiente';
    ELSE
        UPDATE cliente
        SET saldo = saldo - NEW.valor_saque
        WHERE id_cliente = NEW.id_cliente;
    END IF;
END//
DELIMITER ;


DELIMITER //
CREATE TRIGGER antes_deposito
AFTER INSERT ON deposito
FOR EACH ROW
BEGIN
    UPDATE cliente
    SET saldo = saldo + NEW.valor_deposito
    WHERE id_cliente = NEW.id_cliente;
END;
//
DELIMITER ;

/*select nome, saldo from cliente;

insert into deposito (id_agencia, id_cliente, valor_deposito) values (1, 1, 1000);

insert into saque (id_agencia, id_cliente, valor_saque) values (1, 1, 1500);

insert into saque (id_agencia, id_cliente, valor_saque) values (1, 1, 1500);*/