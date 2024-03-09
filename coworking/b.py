import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database = 'TESTE1'
)

cursor = conexao.cursor()
#cursor.execute("SHOW DATABASE")
#MOSTRA BANCO DE DADOS
#cursor.execute("CREATE DATABASE TESTE1")
#CRIANDO TABELA
#cursor.execute("CREATE TABLE alexandria(nome VARCHAR(255), arma VARCHAR(255))")
#CRIANDO TABELA
#cursor.execute("SHOW TABLES")
#MOSTRA TABELAS
#cursor.execute("CREATE TABLE RIOTOP(nome VARCHAR(255), arma VARCHAR(255))")
#CRIANDO TABELA
#cursor.execute("CREATE TABLE COMUNIDADEDOREINO(nome VARCHAR(255), arma VARCHAR(255))")
#CRIANDO TABELA

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)