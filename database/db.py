import sqlite3

def conectar():
    conexao = sqlite3,connect("comandas.db")
    return conexao

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comandas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            mesa TEXT NOT NULL,              
            pedido TEXT NOT NULL,                  
            valor REAL NOT NULL                    
        )
    """)
    
    conexao,commit()
    conexao.close()