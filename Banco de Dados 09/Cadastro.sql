create database clientes;
use clientes;

create table estado(
	id_estado int primary key auto_increment,
    estado varchar(100)
);

create table cidade(
	id_cidade int primary key auto_increment,
    cidade varchar(100),
    id_estado int not null, foreign key (id_estado) references estado(id_estado)
);

create table sexo(
	id_sexo int primary key auto_increment,
    sexo varchar(20)
);

create table nacionalidade(
	id_nacionalidade int primary key auto_increment,
    nacionalidade varchar(30)
);

create table raca(
	id_raca int primary key auto_increment,
    raca varchar(50)
);

create table escolaridade(
	id_escolaridade int primary key auto_increment,
    escolaridade varchar(30)
);

create table clientes(
	cpf varchar(11) unique not null primary key,
	nome varchar(100) not null,
	rg varchar(9) unique not null,
	fone varchar(20) unique not null,
	id_sexo int not null, foreign key (id_sexo) references sexo(id_sexo),
	id_cidade int not null, foreign key (id_cidade) references cidade(id_cidade),
	id_nacionalidade int not null, foreign key (id_nacionalidade) references nacionalidade(id_nacionalidade),
	id_raca int not null, foreign key (id_raca) references raca(id_raca),
	id_escolaridade int not null, foreign key (id_escolaridade) references escolaridade(id_escolaridade)
);

-- Inserção de dados
insert into estado values
(null, 'AC'),
(null, 'AL'),
(null, 'AM'),
(null, 'AP'),
(null, 'BA'),
(null, 'CE'),
(null, 'DF'),
(null, 'ES'),
(null, 'GO'),
(null, 'MA'),
(null, 'MT'),
(null, 'MS'),
(null, 'MG'),
(null, 'PA'),
(null, 'PB'),
(null, 'PR'),
(null, 'PE'),
(null, 'PI'),
(null, 'RJ'),
(null, 'RN'),
(null, 'RS'),
(null, 'RO'),
(null, 'RR'),
(null, 'SC'),
(null, 'SP'),
(null, 'SE'),
(null, 'TO');

insert into cidade values
(null, 'Rio Branco', 1),
(null, 'Cruzeiro do Sul', 1),
(null, 'Sena Madureira', 1),
(null, 'Tarauacá', 1),
(null, 'Feijó', 1),
(null, 'Maceió', 2),
(null, 'Arapiraca', 2),
(null, 'Palmeira dos Índios', 2),
(null, 'São Miguel dos Campos', 2),
(null, 'Penedo', 2),
(null, 'Macapá', 3),
(null, 'Santana', 3),
(null, 'Laranjal do Jari', 3),
(null, 'Oiapoque', 3),
(null, 'Tartarugalzinho', 3),
(null, 'Manaus', 4),
(null, 'Parintins', 4),
(null, 'Itacoatiara', 4),
(null, 'Coari', 4),
(null, 'Manacapuru', 4),
(null, 'Salvador', 5),
(null, 'Feira de Santana', 5),
(null, 'Vitória da Conquista', 5),
(null, 'Ilhéus', 5),
(null, 'Juazeiro', 5),
(null, 'Fortaleza', 6),
(null, 'Juazeiro do Norte', 6),
(null, 'Sobral', 6),
(null, 'Caucaia', 6),
(null, 'Crato', 6),
(null, 'Brasília', 7),
(null, 'Taguatinga', 7),
(null, 'Ceilândia', 7),
(null, 'Samambaia', 7),
(null, 'Planaltina', 7),
(null, 'Vitória', 8),
(null, 'Vila Velha', 8),
(null, 'Serra', 8),
(null, 'Cachoeiro de Itapemirim', 8),
(null, 'Linhares', 8),
(null, 'Goiânia', 9),
(null, 'Anápolis', 9),
(null, 'Rio Verde', 9),
(null, 'Formosa', 9),
(null, 'Catalão', 9),
(null, 'São Luís', 10),
(null, 'Imperatriz', 10),
(null, 'Caxias', 10),
(null, 'Timon', 10),
(null, 'Bacabal', 10),
(null, 'Cuiabá', 11),
(null, 'Várzea Grande', 11),
(null, 'Rondonópolis', 11),
(null, 'Sinop', 11),
(null, 'Tangará da Serra', 11),
(null, 'Campo Grande', 12),
(null, 'Dourados', 12),
(null, 'Três Lagoas', 12),
(null, 'Corumbá', 12),
(null, 'Ponta Porã', 12),
(null, 'Belo Horizonte', 13),
(null, 'Uberlândia', 13),
(null, 'Juiz de Fora', 13),
(null, 'Contagem', 13),
(null, 'Montes Claros', 13),
(null, 'Belém', 14),
(null, 'Ananindeua', 14),
(null, 'Santarém', 14),
(null, 'Marabá', 14),
(null, 'Parauapebas', 14),
(null, 'João Pessoa', 15),
(null, 'Campina Grande', 15),
(null, 'Santa Rita', 15),
(null, 'Bayeux', 15),
(null, 'Patos', 15),
(null, 'Curitiba', 16),
(null, 'Londrina', 16),
(null, 'Maringá', 16),
(null, 'Ponta Grossa', 16),
(null, 'Foz do Iguaçu', 16),
(null, 'Recife', 17),
(null, 'Olinda', 17),
(null, 'Jaboatão dos Guararapes', 17),
(null, 'Caruaru', 17),
(null, 'Petrolina', 17),
(null, 'Teresina', 18),
(null, 'Parnaíba', 18),
(null, 'Picos', 18),
(null, 'Floriano', 18),
(null, 'Oeiras', 18),
(null, 'Rio de Janeiro', 19),
(null, 'Niterói', 19),
(null, 'Duque de Caxias', 19),
(null, 'São Gonçalo', 19),
(null, 'Nova Iguaçu', 19),
(null, 'Natal', 20),
(null, 'Mossoró', 20),
(null, 'Parnamirim', 20),
(null, 'Caicó', 20),
(null, 'São Gonçalo do Amarante', 20),
(null, 'Porto Alegre', 21),
(null, 'Caxias do Sul', 21),
(null, 'Pelotas', 21),
(null, 'Santa Maria', 21),
(null, 'Gravataí', 21),
(null, 'Porto Velho', 22),
(null, 'Ji-Paraná', 22),
(null, 'Vilhena', 22),
(null, 'Ariquemes', 22),
(null, 'Cacoal', 22),
(null, 'Boa Vista', 23),
(null, 'Rorainópolis', 23),
(null, 'Caracaraí', 23),
(null, 'Alto Alegre', 23),
(null, 'Mucajaí', 23),
(null, 'Florianópolis', 24),
(null, 'Joinville', 24),
(null, 'Blumenau', 24),
(null, 'Chapecó', 24),
(null, 'Itajaí', 24),
(null, 'São Paulo', 25),
(null, 'Campinas', 25),
(null, 'Sorocaba', 25),
(null, 'Santos', 25),
(null, 'Ribeirão Preto', 25),
(null, 'Aracaju', 26),
(null, 'Itabaiana', 26),
(null, 'Lagarto', 26),
(null, 'São Cristóvão', 26),
(null, 'Nossa Senhora do Socorro', 26),
(null, 'Palmas', 27),
(null, 'Araguaína', 27),
(null, 'Gurupi', 27),
(null, 'Porto Nacional', 27),
(null, 'Colinas do Tocantins', 27);

insert into sexo values 
(null, 'feminino'),
(null, 'masculino'),
(null, 'outro');

insert into raca values
(null, 'Branco'),
(null, 'Negro'),
(null, 'Indígena'),
(null, 'Asiático'),
(null, 'Caucasiano');

insert into nacionalidade values
(null, 'Brasileiro'),
(null, 'Americano'),
(null, 'Chinês'),
(null, 'Alemão'),
(null, 'Francês');

insert into escolaridade values
(null, 'Ensino Fundamental Incompleto'),
(null, 'Ensino Fundamental Completo'),
(null, 'Ensino Médio Incompleto'),
(null, 'Ensino Médio Completo'),
(null, 'Ensino Superior Completo');

INSERT INTO clientes (cpf, nome, rg, fone, id_sexo, id_cidade, id_nacionalidade, id_raca, id_escolaridade) VALUES
('12345678901', 'Ana Silva', '123456789', '(11) 98765-4321', 1, 1, 1, 1, 4),
('23456789012', 'Carlos Souza', '234567890', '(21) 97654-3210', 2, 2, 2, 2, 5),
('34567890123', 'Maria Oliveira', '345678901', '(31) 96543-2109', 1, 3, 3, 3, 3),
('45678901234', 'José Santos', '456789012', '(41) 95432-1098', 2, 4, 4, 4, 2),
('56789012345', 'Patrícia Costa', '567890123', '(51) 94321-0987', 1, 5, 5, 5, 1),
('67890123456', 'Lucas Almeida', '678901234', '(61) 93210-9876', 2, 6, 1, 2, 5),
('78901234567', 'Fernanda Pereira', '789012345', '(71) 92109-8765', 1, 7, 2, 3, 4),
('89012345678', 'Roberto Lima', '890123456', '(81) 91098-7654', 2, 8, 3, 4, 3),
('90123456789', 'Juliana Fernandes', '901234567', '(91) 90987-6543', 1, 9, 4, 5, 2),
('01234567890', 'Rafael Rodrigues', '012345678', '(11) 89876-5432', 2, 10, 5, 1, 1),
('12345678902', 'Larissa Martins', '123456780', '(21) 88765-4321', 1, 11, 1, 2, 5),
('23456789023', 'Gabriel Costa', '234567890', '(31) 87654-3210', 2, 12, 2, 3, 4),
('34567890134', 'Isabela Silva', '345678901', '(41) 86543-2109', 1, 13, 3, 4, 3),
('45678901245', 'Thiago Oliveira', '456789012', '(51) 85432-1098', 2, 14, 4, 5, 2),
('56789012356', 'Amanda Santos', '567890123', '(61) 84321-0987', 1, 15, 5, 1, 1),
('67890123467', 'Pedro Lima', '678901234', '(71) 83210-9876', 2, 16, 1, 2, 5),
('78901234578', 'Beatriz Almeida', '789012345', '(81) 82109-8765', 1, 17, 2, 3, 4),
('89012345689', 'Marcelo Pereira', '890123456', '(91) 81098-7654', 2, 18, 3, 4, 3),
('90123456790', 'Juliana Martins', '901234567', '(11) 80987-6543', 1, 19, 4, 5, 2),
('01234567891', 'Lucas Rodrigues', '012345678', '(21) 79876-5432', 2, 20, 5, 1, 1);

SELECT c.*, s.sexo, ci.cidade, e.estado, n.nacionalidade, r.raca, esc.escolaridade 
FROM clientes c 
JOIN sexo s ON c.id_sexo = s.id_sexo 
JOIN cidade ci ON c.id_cidade = ci.id_cidade 
JOIN estado e ON ci.id_estado = e.id_estado 
JOIN nacionalidade n ON c.id_nacionalidade = n.id_nacionalidade 
JOIN raca r ON c.id_raca = r.id_raca 
JOIN escolaridade esc ON c.id_escolaridade = esc.id_escolaridade;


