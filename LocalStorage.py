import customtkinter as ctk
import tkinter 
from tkinter import *
from tkinter import messagebox

ctk.set_appearance_mode('dark')

def adicionar_tarefa():
    tarefa = nova_tarefa.get()
    if tarefa:
        lista_tarefas.insert(0,tarefa)
        nova_tarefa.delete(0,END)
    else:
        messagebox.showerror('Erro no APP','Digite uma tarefa seu puto!')
        
def remover_tarefa():
    tarefa_selecionada = lista_tarefas.curselection()
    if tarefa_selecionada:
        lista_tarefas.delete(tarefa_selecionada)
        messagebox.showinfo('DELETADO','Apagado com Sucesso')
    else:
        messagebox.showerror('Erro no APP','Olhe seu burro, selecione uma pohaa ai')    

janela = ctk.CTk()
janela.geometry('300x480')
janela.title('APP Tarefas V1.0')

ctk.CTkLabel(janela,text='APP Tarefas',font=('Arial', 25,'bold'),text_color='green').pack(pady=10)

add_tarefas = ctk.CTkButton(janela,text='Adicionar Tarefa',fg_color='blue',width=100,height=20,command=adicionar_tarefa)
add_tarefas.place(x=30,y=80)
remove_tarefas = ctk.CTkButton(janela,text='Remover Tarefa',fg_color='red',width=100,height=20,command=remover_tarefa)
remove_tarefas.place(x=170,y=80)

nova_tarefa = ctk.CTkEntry(janela,width=250,height=30,placeholder_text='Digite a nova tarefa')
nova_tarefa.pack(pady=100)

ctk.CTkLabel(janela,text='Tarefas Pendentes',font=('Arial', 14,'bold'),text_color='#C9C728').place(x=75,y=200)

lista_tarefas = Listbox(janela,width=40,height=15)
lista_tarefas.place(x=25,y=230)

janela.mainloop()