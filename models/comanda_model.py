from database.db import conectar

def criar_comanda(mesa, pedido, valor):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("""
        INSERT INTO comandas (mesa, pedido, valor)
        VALUES (?, ?, ?)
        """, (mesa, pedido, valor))
    
    conexao.commit()
    conexao.close()
    
    def listar_comandas():
        conexao = conectar()
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM comandas")
        
        registros = cursor.fetchall()
        conexao.close()
        
        return registros
    
    def atualizar_comanda(id_comanda, mesa, pedido, valor):
        conexao = conectar()
        cursor = conexao.cursor()
        
        cursor.execute("""
            UPDATE comandas
            SET mesa = ?, pedido = ?, valor = ?
            WHERE id = ?
            """, (mesa, pedido, valor, id_comanda))
        
        conexao.commit()
        conexao.close()
        
        def deletar_comanda(id_comanda):
            conexao = conectar()
            cursor = conexao.cursor()
            
            cursor.execute("DELETE FROM comandas WHERE id = ?", (id_comanda,))
            
            conexao.commit()
            conexao.close()