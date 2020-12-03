import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Você gostaria de gerar um novo valor para o dado?"
        #layout
        self.layout = [
            [sg.Text('Jogar o Dado?')], 
            [sg.Button('Sim'), sg.Button('Não')]
        ]
       

    def Iniciar(self):
         #criar janela
        self.janela = sg.Window('Simulador de Dado', self.layout)

        #ler eventos
        self.eventos, self.valores = self.janela.Read()

        if self.eventos == "Sim":
        #resposta = input(self.mensagem)
        #if resposta.upper() == "SIM":
            self.GerarValordDoDado()


    def GerarValordDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

print("Marcelo") ##mudar isso no futuro!!!
a = SimuladorDeDado()
a.Iniciar()