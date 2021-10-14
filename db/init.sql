CREATE DATABASE frutas;
use frutas;

CREATE TABLE cores (
  nome VARCHAR(20),
  cor VARCHAR(10)
);

INSERT INTO cores
  (nome, cor)
VALUES
  ('Uva', 'verde'),
  ('Banana', 'amarela');
