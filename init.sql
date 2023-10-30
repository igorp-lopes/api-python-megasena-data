CREATE USER docker;

CREATE DATABASE postgres;

CREATE TABLE megasena_data (
                               concurso SERIAL PRIMARY KEY,
                               data_do_sorteio TIMESTAMP NOT NULL,
                               bola1 INT NOT NULL,
                               bola2 INT NOT NULL,
                               bola3 INT NOT NULL,
                               bola4 INT NOT NULL,
                               bola5 INT NOT NULL,
                               bola6 INT NOT NULL,
                               ganhadores_6_acertos INT NOT NULL,
                               cidade_UF TEXT,
                               rateio_6_acertos TEXT NOT NULL,
                               ganhadores_5_acertos INT NOT NULL,
                               rateio_5_acertos TEXT NOT NULL,
                               ganhadores_4_acertos INT NOT NULL,
                               rateio_4_acertos TEXT NOT NULL,
                               acumulado_6_acertos TEXT NOT NULL,
                               arrecadacao_total TEXT NOT NULL,
                               estimativa_premio TEXT NOT NULL,
                               acumulado_sorteio_especial_mega_da_virada TEXT NOT NULL,
                               observacao TEXT
);

GRANT ALL PRIVILEGES ON DATABASE postgres TO docker;
