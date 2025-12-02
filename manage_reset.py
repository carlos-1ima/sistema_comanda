from database.db import DB_PATH, resetar
from pathlib import Path
import sys

print("Arquivo do DB esperado em:", DB_PATH)

if not DB_PATH.exists():
    print("Arquivo não encontrado — nada para apagar.")
else:
    try:
        resetar()
        print("Banco resetado com sucesso.")
    except PermissionError as e:
        print("ERRO: Permissão negada ao tentar remover o arquivo. Feche o aplicativo que está usando o banco e tente novamente.")
        print("Detalhe:", e)
        sys.exit(1)
    except Exception as e:
        print("Erro ao resetar:", e)
        sys.exit(2)