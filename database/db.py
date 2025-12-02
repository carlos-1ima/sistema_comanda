import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # vai para a raiz do projeto
DB_PATH = BASE_DIR / "comandas.db"

def conectar():
    return sqlite3.connect(str(DB_PATH))

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
    
    conexao.commit()
    conexao.close()

def resetar():
    try:
        tmp = sqlite3.connect(str(DB_PATH))
        tmp.close()
    except Exception:
        pass
    
    if DB_PATH.exists():
        try:
            DB_PATH.unlink()
        except PermissionError as e:
            raise PermissionError(f"Não foi possível remover {DB_PATH!s}: {e}")
            
    criar_tabelas()
    
criar_tabelas()