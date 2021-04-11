-- MySQL Script generated by MySQL Workbench
-- Sun Apr 11 00:03:06 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering
-- Scrapping Facebook Data Base
-- Guerra Cervantes Sergio Enrique

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;


-- -----------------------------------------------------
-- Table Post
-- -----------------------------------------------------
DROP TABLE IF EXISTS Post ;

CREATE TABLE IF NOT EXISTS Post (
  idPost INT NOT NULL,
  URL VARCHAR(45) NOT NULL,
  Persona VARCHAR(45) NOT NULL,
  Texto VARCHAR(200) NULL,
  PRIMARY KEY (idPost),
  UNIQUE INDEX idPost_UNIQUE (idPost))
;


-- -----------------------------------------------------
-- Table Comentarios
-- -----------------------------------------------------
DROP TABLE IF EXISTS Comentarios ;

CREATE TABLE IF NOT EXISTS Comentarios (
  idComentarios INT NOT NULL AUTO_INCREMENT,
  Post_idPost INT NOT NULL,
  Persona VARCHAR(45) NOT NULL,
  Texto VARCHAR(45) NULL,
  PRIMARY KEY (idComentarios, Post_idPost),
  FOREIGN KEY (Post_idPost)
  REFERENCES Post (idPost))
;


-- -----------------------------------------------------
-- Table Respuesta
-- -----------------------------------------------------
DROP TABLE IF EXISTS Respuesta ;

CREATE TABLE IF NOT EXISTS Respuesta (
  idRespuesta INT NOT NULL AUTO_INCREMENT,
  Persona VARCHAR(45) NULL,
  Texto VARCHAR(100) NOT NULL,
  Comentarios_idComentarios INT NOT NULL,
  Post_idPost INT NOT NULL,
  PRIMARY KEY (idRespuesta, Comentarios_idComentarios, Post_idPost),
  FOREIGN KEY (Comentarios_idComentarios , Post_idPost)
  REFERENCES Comentarios (idComentarios , Post_idPost))
;


-- -----------------------------------------------------
-- Table Compartir
-- -----------------------------------------------------
DROP TABLE IF EXISTS Compartir ;

CREATE TABLE IF NOT EXISTS Compartir (
  idCompartir INT NOT NULL AUTO_INCREMENT,
  Post_idPost INT NOT NULL,
  Persona VARCHAR(45) NULL,
  PRIMARY KEY (idCompartir, Post_idPost),
  FOREIGN KEY (Post_idPost)
  REFERENCES Post (idPost))
;


-- -----------------------------------------------------
-- Table Reacciones
-- -----------------------------------------------------
DROP TABLE IF EXISTS Reacciones ;

CREATE TABLE IF NOT EXISTS Reacciones (
  idReacciones INT NOT NULL AUTO_INCREMENT,
  Tipo VARCHAR(45) NULL,
  Persona VARCHAR(45) NULL,
  Post_idPost INT NOT NULL,
  PRIMARY KEY (idReacciones, Post_idPost),
  FOREIGN KEY (Post_idPost)
  REFERENCES Post (idPost))
;

SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;