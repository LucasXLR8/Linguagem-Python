import customtkinter as ctk

#FUNÇOES-----------------------
def formula():
    n1 = float(nota1.get())
    n2 = float(nota2.get())
    n3 = float(nota3.get())
    
    media = (n1+n2+n3)/3
    
    if(media >=7):
        resultado.configure(text=f'Sua media foi {media:.1f} \n voce foi APROVADO!')
    else:
        resultado.configure(text=f'Sua media foi {media:.1f} \n voce foi para RECUPERAÇÃO!')

def limpar():
    nota1.delete(0,'end')
    nota2.delete(0,'end')
    nota3.delete(0,'end')
    resultado.configure(text='')

ctk.set_appearance_mode('dark')

janela = ctk.CTk()
janela.minsize(600,400)
janela.title('Sistema escolar V1.0')

ctk.CTkLabel(janela,text='Sistema Escolar versao 1.0',font=('Arial',27,'bold'),text_color='green').pack(pady=5)

nota1 = ctk.CTkEntry(janela,placeholder_text='Digite a nota da primeira unidade',width=400,height=30)
nota1.pack(pady=10)
nota2 = ctk.CTkEntry(janela,placeholder_text='Digite a nota da segunda unidade',width=400,height=30)
nota2.pack(pady=10)
nota3 = ctk.CTkEntry(janela,placeholder_text='Digite a nota da terceira unidade',width=400,height=30)
nota3.pack(pady=10)

btn = ctk.CTkButton(janela,text='Calcular',fg_color='green',text_color='white',width=100,height=30,cursor='hand2',command=formula)
btn.pack(pady=10)
btnLimpar = ctk.CTkButton(janela,text='Limpar',fg_color='darkred',text_color='white',width=100,height=30,cursor='hand2',command=limpar)
btnLimpar.pack(pady=10)

resultado = ctk.CTkLabel(janela,text='',font=('Arial',20,'bold'),text_color='white')
resultado.pack(pady=5)

janela.mainloop()