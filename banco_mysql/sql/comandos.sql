create database udemy_neri;

use udemy_neri;

create table pessoas(id int NOT NULL AUTO_INCREMENT, nome varchar(50) not NULL, 
email varchar(100), idade int(3), PRIMARY KEY(id));

-- ALTER TABLE "table_name" RENAME COLUMN "column 1" TO "column 2";
-- ALTER TABLE clientes RENAME COLUMN aniversario TO aniversario_clientes;