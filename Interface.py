import PySimpleGUI as sg

class InterfaceQuizz:
    
    def __init__(self):
        sg.change_look_and_feel('BlueMono')
        
        #Layout
        
        layout = [
            [sg.Text('Questão 1: Qual das seguintes proposições está gramaticalmente correta?',size = (70,3))],
            [sg.Radio('a)Durante a pandemia, brasileiros tiveram uma perca significante de familiares','resposta', key = 'letraa')],
            [sg.Radio('b)Letra b','resposta', key = 'letrab')],
            [sg.Radio('c)Não perda tempo','resposta', key = 'letrac')],
            [sg.Radio('d)Depois do trauma ocorrido, ele teve uma perda de memória considerável','resposta', key = 'letrad')],
            [sg.Button('Próxima')],
            ] 

        #Janelas
        janela = sg.Window('Tela do Quizz').layout(layout)


        #Extração de dados
        self.button, self.values = janela.Read()
        self.radio, self.values = janela.Read()
        
        
    def Iniciar(self):
        pontuacao = 0
        a = self.values['letraa']
        b = self.values['letrab']
        c = self.values['letrac']
        d = self.values['letrad']

        if d == True:
            pontuacao += 1
        print('Sua pontuacao atual é:{}'.format(pontuacao))

tela = InterfaceQuizz()
tela.Iniciar()
