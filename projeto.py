import tkinter as tk
from tkinter import messagebox

# Configurando a janela principal
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("500x400")
janela.configure(bg="#ADD8E6")  # Azul claro

# Criando os elementos da interface

# Campo de entrada e botão de adicionar
frame_entrada = tk.Frame(janela, bg="#ADD8E6")  # Azul claro
frame_entrada.pack(pady=10)

entrada = tk.Entry(frame_entrada, width=30, font=("Arial", 14))
entrada.pack(side=tk.LEFT, padx=5)

btn_adicionar = tk.Button(frame_entrada, text="Adicionar Tarefa", bg="#4CAF50", fg="white")
btn_adicionar.pack(side=tk.RIGHT)

# Lista de tarefas
frame_lista = tk.Frame(janela, bg="#ADD8E6")  # Azul claro
frame_lista.pack(pady=10)

lista_tarefas = tk.Listbox(frame_lista, width=40, height=10, font=("Arial", 14), selectmode=tk.SINGLE)
lista_tarefas.pack()

# Botões de controle
frame_botoes = tk.Frame(janela, bg="#ADD8E6")  # Azul claro
frame_botoes.pack(pady=10)

btn_remover = tk.Button(frame_botoes, text="Remover Tarefa", bg="#f44336", fg="white")
btn_remover.pack(side=tk.LEFT, padx=10)

btn_concluir = tk.Button(frame_botoes, text="Concluir Tarefa", bg="#2196F3", fg="white")
btn_concluir.pack(side=tk.RIGHT, padx=10)

# Adicionando as funções

def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa.strip():
        lista_tarefas.insert(tk.END, tarefa)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada inválida", "Digite uma tarefa válida!")

def remover_tarefa():
    try:
        tarefa_selecionada = lista_tarefas.curselection()
        lista_tarefas.delete(tarefa_selecionada)
    except:
        messagebox.showwarning("Erro", "Selecione uma tarefa para remover!")

def concluir_tarefa():
    try:
        tarefa_selecionada = lista_tarefas.curselection()
        tarefa = lista_tarefas.get(tarefa_selecionada)
        lista_tarefas.delete(tarefa_selecionada)
        lista_tarefas.insert(tk.END, f"[Concluído] {tarefa}")
    except:
        messagebox.showwarning("Erro", "Selecione uma tarefa para concluir!")

# Conectando os botões às funções
btn_adicionar.config(command=adicionar_tarefa)
btn_remover.config(command=remover_tarefa)
btn_concluir.config(command=concluir_tarefa)

# Iniciar o loop principal da janela
janela.mainloop()
