import sqlite3

conn = sqlite3.connect('Data.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cadastro(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    codigo INT,
    descricao VARCHAR(50),
    preco DOUBLE,
    categoria VARCHAR(20)
);
""")

print("conectando ao banco de dados...")