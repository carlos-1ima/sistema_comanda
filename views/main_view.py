import  tkinter as tk
from tkinter import ttk, messagebox

from models.comanda_model import(
    listar_comandas,
    deletar_comanda
)

from views.comanda_view import abrir_tela_comanda

def abrir_tela_principal():
    janela = tk.Tk()
    janela.title("Sistema Comandas")
    janela.geometry("700x400")
    
    titulo = tk.Label(
        janela,
        text="Sistema Comandas",
        font=("Arial", 18, "bold")
    )
    titulo.pack(pady=10)
    
    colunas = ("ID", "Mesa", "Pedido", "Valor")
    
    tabela = ttk.Treeview(
        janela,
        columns=colunas,
        show="headings"
    )
    
    tabela.heading("ID", text="ID")
    tabela.heading("Mesa", text="Mesa")
    tabela.heading("Pedido", text="Pedido")
    tabela.heading("Valor", text="Valor (R$)")
    
    tabela.column("ID", width=50)
    tabela.column("Mesa", width=80)
    tabela.column("Pedido", width=300)
    tabela.column("Valor", width=100)
    
    tabela.pack(fill="both", expand=True, pady=10)
    
    def carregar_tabela():
        for linha in tabela.get.children():
            tabela.delete(linha)
        
        dados = listar_comandas()
        
        for item in dados:
            tabela.insert("", "end", values=item)
    
    carregar_tabela()
    
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=10)
    
    botao_novo = tk.Button(
        frame_botoes,
        text="Nova Comanda",
        width=15,
        command=lambda: abrir_tela_comanda(carregar_tabela)
    )
    botao_novo.grid(row=0, column=0, padx=10)
    
    def editar():
        item = tabela.focus()
        if not item:
            messagebox.showwarning("Aviso", "Selecione uma comanda para editar.")
            return
        
        valores = tabela.item(item, "values")
        abrir_tela_comanda(carregar_tabela)
        
    botao_editar = tk.Button(
        frame_botoes,
        text="Editar",
        width=15,
        command=editar
    )
    botao_editar.grid(row=0, column=1, padx=10)
    
    def deletar():
        item = tabela.focus()
        if not item:
            messagebox.showwarning("Aviso", "Selecione uma comanda para deletar.")
            return
        
        valores = tabela.item(item, "values")
        id_comanda = valores[0]
        
        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            "Tem certeza que deseja excluir a comanda?"
        )
        
        if confirmar:
            deletar_comanda(id_comanda)
            carregar_tabela()
            
    botao_deletar = tk.Button(
        frame_botoes,
        text="Deletar",
        width=15,
        command=deletar
    )
    botao_deletar.grid(row=0, column=2, padx=10)
    
    janela.mainloop()
    