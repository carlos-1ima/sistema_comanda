import tkinter as tk
from tkinter import messagebox
import csv

from models.comanda_model import listar_comandas, deletar_todas
from database.db import resetar

def abrir_admin():
    janela = tk.Toplevel()
    janela.title("Painel Administrativo")
    janela.geometry("400x400")
    
    titulo = tk.Label(janela, text="Painel Administrativo", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)
    
    def mostrar_quantidade():
        quantidade = len(listar_comandas())
        messagebox.showinfo("Quantidade", f"Total de comandas: {quantidade}")
        
    botao_quantidade = tk.Button(janela, text="Quantidade de Comandas", width=25, command=mostrar_quantidade)
    botao_quantidade.pack(pady=5)

    def mostrar_faturamento():
        dados = listar_comandas()
        total = sum([c[3] for c in dados])
        messagebox.showinfo("Faturamento", f"Faturamento total: R$ {total:.2f}")

    botao_faturamento = tk.Button(janela, text="Faturamento Total", width=25, command=mostrar_faturamento)
    botao_faturamento.pack(pady=5)

    def resetar_banco():
        confirmar = messagebox.askyesno("Confirmar", "Tem certeza que deseja apagar tudo?")
        if confirmar:
            deletar_todas()
            messagebox.showinfo("Ok", "Todas as comandas foram apagadas!")

    botao_reset = tk.Button(janela, text="Resetar Banco", bg="red", fg="white", width=25, command=resetar_banco)
    botao_reset.pack(pady=5)

    def exportar_csv():
        dados = listar_comandas()
        with open("comandas_export.csv", "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["ID", "Mesa", "Pedido", "Valor"])
        
            for c in dados:
                writer.writerow(c)
        messagebox.showinfo("Ok", "Arquivo CSV exportado com sucesso!")
        
    botao_csv = tk.Button(janela, text="Exportar CSV", width=25, command=exportar_csv)
    botao_csv.pack(pady=5)