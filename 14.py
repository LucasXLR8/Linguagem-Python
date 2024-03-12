import customtkinter as ct #IMPORTANDO A BIBLIOTECA

ct.set_appearance_mode('dark') #MUNDANDO A COR DA BORDA DE CIMA DA JANELA

janela = ct.CTk('#434343') #CRIANDO A JANELA
janela.geometry('500x300') #DEFININDO O TAMANHO DA JANELA
janela.title('Tela de Acesso') #TITULO DA JANELA
janela.iconbitmap('icone.ico') #MUDANDO O ICONE DA JANELA
janela.mainloop #PRA JANELAR FICAR SEMPRE ABERTA
