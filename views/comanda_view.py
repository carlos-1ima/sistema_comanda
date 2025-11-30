import tkinter as tk
from tkinter import messagebox

from models.comanda_model import(
    criar_comanda,
    atualizar_comanda
)

def abrir_tela_comanda(recarregar_tabela, dados=None):
    janela = tk.Toplevel()
    janela.title("Cadastro Comanda")
    janela.geometry("400x300")

    label_mesa = tk.Label(janela, text="Mesa")
    label_mesa.pack(pady=5)

    input_mesa = tk.Entry(janela)
    input_mesa.pack()

    label_pedido = tk.Label(janela, text="Pedido:")
    label_pedido.pack(pady=5)

    input_pedido = tk.Entry(janela)
    input_pedido.pack()

    label_valor = tk.Label(janela, text="Valor (R$):")
    label_valor.pack(pady=5)

    input_valor = tk.Entry(janela)
    input_valor.pack()

    id_comanda = None

    if dados:
        id_comanda = dados[0]
        input_mesa.insert(0, dados[1])
        input_pedido.insert(0, dados[2])
        input_valor.insert(0, dados[3])
    
    def salvar():
        mesa = input_mesa.get()
        pedido = input_pedido.get()
        valor = input_valor.get()
        
        if not mesa or not pedido or not valor:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return
        
        try:
            valor = float(valor)
        except:
            messagebox.showwarning("Aviso", "Valor deve ser um número.")
        
        if id_comanda:
            atualizar_comanda(id_comanda, mesa, pedido, valor)
            messagebox.showinfo("Sucesso", "Comanda atualizada com sucesso!")
            
        else:
            criar_comanda(mesa, pedido, valor)
            messagebox.showinfo("Sucesso", "Comanda criada com sucesso!")
        
        recarregar_tabela()
        janela.destroy()
        
    botao_salvar = tk.Button(
        janela, 
        text="Salvar",
        width=15,
        command=salvar
    )
    botao_salvar.pack(pady=20)
        
        
        