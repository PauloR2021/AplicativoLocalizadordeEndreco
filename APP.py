import tkinter
import tkinter.ttk
from tkinter import *
from tkinter import ttk

import API_CEP
import API_END
import pandas as pd


import tkinter.font as tkFont

from tkinter import messagebox
from PIL import Image, ImageTk


""" Desenvolvendo as Funções do APP """

def BuscarCep():

    # Pegando as Informações do Usuário
    CEP= cep.get()
    contador = len(CEP)

    # Criando uma Condição para que se o CEP digitado for igual a 8 digitos ele executa uma função
    # Se a contagem for igual a 8, executa a api: API_CEP.py
    if contador == 8:
        # Criando a Label de Resposta da Requisição da API
        txt_resultado = Label(frame, text='', background=alice_blue)
        txt_resultado.place(y=50, x=250)

        # Solicitando as Informações da API
        requisicao = API_CEP.ApiCep(CEP)

        # Pegando as informações da API
        n_cep = requisicao.REQUISICAO_JSON['cep']
        localidade = requisicao.REQUISICAO_JSON['localidade']
        uf = requisicao.REQUISICAO_JSON['uf']
        ddd = requisicao.REQUISICAO_JSON['ddd']

        # Mostrando o Resultado da API
        txt_resultado['text']=f"CEP: {n_cep}\n" \
                              f"UF: {uf}\n" \
                              f"CIDADE: {localidade}\n" \
                              f"DDD: {ddd}"

        # Limpando a Label para Inserir o CEP
        cep.delete(0,END)

    # Se a contagem for diferente de 8, o programa executa outra função
    else:
        # Mensagem informando o erro para o Usuário
        messagebox.showerror('ErroR', "O CEP Digitado é Incorreto")
        # Limpa o Label para inserir o CEP
        cep.delete(0,END)

def InformacaoEnd():

    #Criando as Funções do Botão para Buscar por Endereço
    def BuscarEnd():

        # Criando a Label da resposta da API
        txt_resultado = Label(frame,text='',background=alice_blue)
        txt_resultado.place(y=40,x=150)

        # Criando as váriaveis para salvar os dados digitados pelo Usuário
        uf = uf_inserir.get()
        cidade = cidade_inserir.get()
        end = end_inserir.get()
        endereco_contagem = len(end)

        requisicao = API_END.ApiEnd(uf,cidade,end)
        REQUISICAO = requisicao.REQUISICAO_JSON

        tabela = pd.DataFrame(REQUISICAO)
        print(tabela)











    """ Criando a Tela para Digitar o Endereço"""
    #Configurando as Label para o Endereço

    #Solicitando a UF = Estado da Cidade
    uf = Label(frame, text='Digite o UF: ',compound=LEFT, bg=alice_blue, relief=FLAT, anchor='center',border=10)
    uf.place(y=160, x=-2)
    uf_inserir = Entry(frame,width=25,bd='6')
    uf_inserir.place(y=200,x=4)

    #Solicitando o Nome da Cidade
    cidade = Label(frame, text='Digite a Cidade: ', compound=LEFT, bg=alice_blue, relief=FLAT, anchor='center', border=10)
    cidade.place(y=230, x=-10)
    cidade_inserir = Entry(frame, width=25, bd='6')
    cidade_inserir.place(y=280, x=4)

    # Solicitando o Enderço
    end_nome = Label(frame, text='Digite o Endereço: ', compound=LEFT, bg=alice_blue, relief=FLAT, anchor='center',border=10)
    end_nome.place(y=310, x=-2)
    end_inserir = Entry(frame, width=25, bd='6')
    end_inserir.place(y=350, x=4)

    buscar_end = Button(frame, text='BUSCAR ENDEREÇO', command=BuscarEnd, background=alice_blue)
    buscar_end.place(y=390, x=4)




""" Desenvolvendo o APP """

# Cores do APP
branco = "#FFFFFF"
neve = "#FFFAFA"
azul_neve = "#F0FFFF"
alice_blue = "#F0F8FF"
fastama_branco = "#F8F8FF"

# Crindo Janela do (APLICATIVO)
app = Tk()
app.title("Busca CEP")
app.geometry('800x800')
app.configure(bg=alice_blue)

# Criando os Frames do APP
frame = Frame(app, width=800, height=800, bg=alice_blue, pady=0, padx=0, relief='flat',borderwidth='10')
frame.grid(row=1,column=0)

# Fontes do APP


# Icone do APP
# TreVeiw

tabela_head = ['Nome', 'Código', 'Local', 'Data', 'Quantidade', 'Valor']

# criando a tabela
tree = app.Treeview(frame, selectmode="extended", columns=tabela_head, show="headings")

# vertical scrollbar
vsb = app.Scrollbar(frame, orient="vertical", command=tree.yview)

# horizontal scrollbar
hsb = app.Scrollbar(frame, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

frame.grid_rowconfigure(0, weight=12)

hd = ["nw", "nw", "nw", "nw", "nw", "center", "center"]
h = [30, 170, 140, 100, 120, 50, 100]
n = 0

for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    # adjust the column's width to the header string
    tree.column(col, width=h[n], anchor=hd[n])

    n += 1
# Inserindo Objetos na Tela
# Pedindo para o Usuário o CEP
cep_cidade = Label(frame, text='Digite um CEP:',compound=LEFT, bg=alice_blue, relief=FLAT, anchor='center',border=20)
cep_cidade.place(y=2, x=-12)
#Label para o Usuário digitar o CEP

cep = Entry(frame, width=25,bd='6')
cep.place(y=50,x=4)

#Criando o Botão para a Consulta

buscar = Button(frame,text='BUSCAR',command=BuscarCep,background=alice_blue)
buscar.place(y=90,x= 8)

# Criando um Botão para Mostrar As Informações para Preencher

endereco = Button(frame,text='Inserir Endereço',command=InformacaoEnd,background=alice_blue)
endereco.place(y=130,x=8)

app.mainloop()