DROP DATABASE indecoders;
DROP USER   idcuser;

CREATE DATABASE indecoders;
CREATE USER idcuser WITH PASSWORD 'idc';
GRANT ALL PRIVILEGES ON DATABASE indecoders TO idcuser;