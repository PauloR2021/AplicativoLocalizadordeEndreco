import requests
import pandas as pd
from tkinter import *
from tkinter import messagebox

class ApiEnd:

    def __init__(self,uf,cidade,end):
        self.UF = uf
        self.CIDADE = cidade
        self.END = end

        self.LINK = f'https://viacep.com.br/ws/{self.UF}/{self.CIDADE}/{self.END}/json/'
        self.REQUISICAO = requests.get(self.LINK)

        self.REQUISICAO_JSON = self.REQUISICAO.json()



