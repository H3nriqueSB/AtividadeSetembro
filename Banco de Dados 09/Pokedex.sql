CREATE DATABASE pokemon;
USE pokemon;

CREATE TABLE pokedex(
	nome varchar(12) primary key,
	tipo varchar(12),
    especie varchar(50),
    altura varchar(50),
    largura varchar(50),
    habilidade varchar(50),
    catch_rate varchar(50),
    base_amizade varchar(50),
    base_exp varchar(50),
    crescimento varchar(50),
    genero varchar(50),
    hp varchar(50),
    attack varchar(50),
    defesa varchar(50),
    special_attack varchar(50),
    special_defesa varchar(50),
    velocidade varchar(50)
    );
    
    select * from pokedex;
	select count(nome) from pokedex where nome like 'A%';
	select count(tipo) from pokedex where tipo = 'Grass';
	select count(especie) from pokedex where especie like 'Ice%';
	select count(altura) from pokedex where altura > 3;
	select count(largura) from pokedex where largura < 25;
	select count(habilidade) from pokedex where habilidade like '1. Levitate%';
	select count(catch_rate) from pokedex where catch_rate = 100;
	select count(base_amizade) from pokedex where base_amizade = 50;
	select count(base_exp) from pokedex where base_exp = 0;
	select count(peso) from pokedex where peso > 3; 
	select count(crescimento) from pokedex where crescimento like 'Fast%';
	select count(genero) from pokedex where genero like 'genderless%';
	select count(hp) from pokedex where hp > 100;
	select count(attack) from pokedex where attack > 100;
	select count(defesa) from pokedex where defesa > 100;
	select count(special_attack) from pokedex where special_attack > 100;
	select count(special_defesa) from pokedex where special_defesa > 100;
	select count(velocidade) from pokedex where velocidade > 100;
    
	select count(*) from pokedex where tipo = 'Grass' and hp < 100;