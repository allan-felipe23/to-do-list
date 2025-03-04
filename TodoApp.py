import tkinter as tk
from tkinter import ttk, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        self.root.geometry("500x400")
        self.root.resizable(True, True)  # Permite redimensionar a janela

        # Configuração de estilo
        self.style = ttk.Style()
        self.style.configure("TButton", padding=5, font=("Helvetica", 10))
        self.style.configure("TEntry", padding=5, font=("Helvetica", 12))
        self.style.configure("TListbox", font=("Helvetica", 12))

        # Lista para armazenar as tarefas
        self.tasks = []

        # Frame principal
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Campo de entrada para novas tarefas
        self.task_entry = ttk.Entry(self.main_frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # Botão para adicionar tarefas
        self.add_button = ttk.Button(
            self.main_frame, text="Adicionar Tarefa", command=self.add_task
        )
        self.add_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Lista de tarefas
        self.task_listbox = tk.Listbox(
            self.main_frame, width=50, height=15, font=("Helvetica", 12)
        )
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Botão para remover tarefas selecionadas
        self.remove_button = ttk.Button(
            self.main_frame, text="Remover Tarefa Selecionada", command=self.remove_task
        )
        self.remove_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Configuração do grid para expansão
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

    def add_task(self):
        """Adiciona uma nova tarefa à lista."""
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Por favor, insira uma tarefa.")

    def remove_task(self):
        """Remove a tarefa selecionada da lista."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index)
        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()