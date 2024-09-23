import tkinter as tk
from tkinter import messagebox


def mostrar_texto():
    # Exibe o texto inserido no Entry
    texto = entrada.get()
    label_texto["text"] = f"Você digitou: {texto}"


def marcar_opcao():
    # Exibe a opção marcada no radiobutton
    opcao_selecionada = opcao_var.get()
    messagebox.showinfo("Opção selecionada", f"Você escolheu: {opcao_selecionada}")


def mostrar_check():
    # Exibe as opções de checkboxes selecionadas
    resultado = []
    if check1_var.get():
        resultado.append("Opção 1")
    if check2_var.get():
        resultado.append("Opção 2")
    if check3_var.get():
        resultado.append("Opção 3")

    messagebox.showinfo("Checkboxes", f"Você marcou: {', '.join(resultado)}")


def adicionar_item():
    # Adiciona um item à listbox
    item = entrada.get()
    listbox.insert(tk.END, item)


def remover_item():
    # Remove o item selecionado da listbox
    selecionado = listbox.curselection()
    if selecionado:
        listbox.delete(selecionado)


# Janela principal
root = tk.Tk()
root.title("Resumo das Funcionalidades do Tkinter")
root.geometry("400x400")

# Entry para entrada de texto
entrada = tk.Entry(root, width=30)
entrada.pack(pady=5)

# Botão para exibir o texto inserido
btn_mostrar_texto = tk.Button(root, text="Mostrar Texto", command=mostrar_texto)
btn_mostrar_texto.pack(pady=5)

# Label para exibir o texto inserido
label_texto = tk.Label(root, text="Texto aparecerá aqui", bg="lightgray", width=30)
label_texto.pack(pady=5)

# Radio buttons
opcao_var = tk.StringVar(value="Opção A")
radio1 = tk.Radiobutton(root, text="Opção A", variable=opcao_var, value="Opção A")
radio2 = tk.Radiobutton(root, text="Opção B", variable=opcao_var, value="Opção B")
radio3 = tk.Radiobutton(root, text="Opção C", variable=opcao_var, value="Opção C")

radio1.pack(anchor="w")
radio2.pack(anchor="w")
radio3.pack(anchor="w")

# Botão para exibir a opção selecionada nos Radio buttons
btn_opcao = tk.Button(root, text="Mostrar Opção", command=marcar_opcao)
btn_opcao.pack(pady=5)

# Checkbuttons (caixas de seleção)
check1_var = tk.BooleanVar()
check2_var = tk.BooleanVar()
check3_var = tk.BooleanVar()

check1 = tk.Checkbutton(root, text="Opção 1", variable=check1_var)
check2 = tk.Checkbutton(root, text="Opção 2", variable=check2_var)
check3 = tk.Checkbutton(root, text="Opção 3", variable=check3_var)

check1.pack(anchor="w")
check2.pack(anchor="w")
check3.pack(anchor="w")

# Botão para exibir as caixas de seleção marcadas
btn_checks = tk.Button(root, text="Mostrar Checkboxes", command=mostrar_check)
btn_checks.pack(pady=5)

# Listbox
listbox = tk.Listbox(root)
listbox.pack(pady=5)

# Botões para adicionar e remover itens da listbox
btn_adicionar = tk.Button(root, text="Adicionar Item", command=adicionar_item)
btn_adicionar.pack(pady=5)

btn_remover = tk.Button(root, text="Remover Item Selecionado", command=remover_item)
btn_remover.pack(pady=5)

# Loop principal da aplicação
root.mainloop()
