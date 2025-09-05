Instructions:

Crear venv en este directorio
source bin/activate
pip3 install -r requirements.txt
deactivate

Logearse en PSQL con superuser

CREATE DATABASE aqua;
CREATE USER mi_usuario WITH ENCRYPTED PASSWORD 'mi_contraseña';
GRANT ALL PRIVILEGES ON DATABASE aqua to aqua
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO aqua;
CREATE EXTENSION IF NOT EXISTS adminpack;

pg_restore -U aqua -d aqua -W -v --no-owner --role=aqua "FILE"

