import mysql.connector
#mysql-connector-python 8.4.0

# Establish connection to MySQL database
try:
    cnx = mysql.connector.connect(
        host='127.0.0.1',
        port='33060',
        user='root',
        password='secret',
        database='azure_mysql'
    )

    # For example, create a cursor to execute SQL queries
    cursor = cnx.cursor()

    # Execute a query
    query = "SELECT * FROM medico"
    cursor.execute(query)

    # Fetch results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")



"""
create database azure_mysql;

CREATE TABLE IF NOT EXISTS medico(
	pk INT UNSIGNED NOT NULL AUTO_INCREMENT,
	nombre varchar(50) NOT NULL,
	ap_paterno varchar(50) NOT NULL,
	ap_materno varchar(50) NOT NULL,
	esp varchar(50) NOT NULL,
	PRIMARY KEY (pk)
);

CREATE TABLE IF NOT EXISTS consultorio(
	pk INT UNSIGNED NOT NULL AUTO_INCREMENT,
	numero INT NOT NULL,
	piso INT NOT NULL,
	PRIMARY KEY (pk)
);


CREATE TABLE IF NOT EXISTS cita(
	pk INT UNSIGNED NOT NULL AUTO_INCREMENT,
	fecha_creacion DATETIME NOT NULL,
	fecha_consulta DATETIME NOT NULL,
	nombre_paciente varchar(60) NOT NULL,
	estado INT NOT NULL,
	fk_consultorio INT UNSIGNED NOT NULL,
	fk_medico INT UNSIGNED NOT NULL,
	PRIMARY KEY (pk),
	FOREIGN KEY (fk_consultorio) REFERENCES consultorio(pk),
	FOREIGN KEY (fk_medico) REFERENCES medico(pk)
);

insert into medico(nombre, ap_paterno, ap_materno, esp)values("dr simi", "simi", "perez", "medico cirujano");
insert into consultorio(numero, piso)values(1, 1);
"""