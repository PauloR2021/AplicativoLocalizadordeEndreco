import requests
from tkinter import *
from tkinter import messagebox

"""Possiveis Códigos de Retorno da API"""
"""200- Deu Certo a API"""
"""402 - API não Conectada"""
"""500 - Servidor Indisponivel"""

""" Criando uma Classe para a API """


class ApiCep:


    def __init__(self, cep):
        try:
            self.CEP = cep
            self.LINK = f'https://viacep.com.br/ws/{self.CEP}/json/'

            self.REQUISICAO = requests.get(self.LINK)

            self.REQUISICAO_JSON = self.REQUISICAO.json()

            localidade = self.REQUISICAO_JSON['localidade']
            print(localidade)

        except:
            messagebox.showerror('ERROR','CEP Não Encontrado')

teste= ApiCep('84990000')
print(teste)