import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import read_all_windows
pontuacao = 0 


def questao(numero):
    #Layout
    sg.theme('reddit')
    layout = [
        [sg.Text('Enunciado',size = (70,3))],
        [sg.Radio('a)Alternativa A','resposta', key = f'letraa{numero}')],
        [sg.Radio('b)Alternativa B','resposta', key = f'letrab{numero}')],
        [sg.Radio('c)Alternativa C','resposta', key = f'letrac{numero}')],
        [sg.Radio('d)Alternativa D','resposta', key = f'letrad{numero}')],
        ] 
    return layout

layout = [[sg.Column(questao(i + 1), key=f'-COL{i + 1}-', visible=(i==0)) for i in range(3)],
        [sg.Button('Prox'), sg.Button('Exit')]]

window = sg.Window('Swapping the contents of a window', layout)

layout = 1  # The currently visible layout

#criar um loop de leitura de eventos 

while True:
    event, values = window.read()
    print(f'evento:{event}\nvalor:{values}')
    if event is 'Exit':
        break

    if event == 'Prox':
        # '-COL2
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout + 1 if layout < 3 else 1
        window[f'-COL{layout}-'].update(visible=True)

#lógica do que deve acontecer ao clicar nos botoes
