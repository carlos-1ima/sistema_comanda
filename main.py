from views.main_view import abrir_tela_principal
from database.db import criar_tabelas

def main():
    criar_tabelas()
    abrir_tela_principal()
    
if __name__ == "__main__":
    main()