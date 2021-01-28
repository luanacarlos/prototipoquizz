import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import read_all_windows
pontuacao = 0 


def questao1():
        
    #Layout
    sg.theme('reddit')
    layout = [
        [sg.Text('Enunciado',size = (70,3))],
        [sg.Radio('a)Alternativa A','resposta', key = 'letraa1')],
        [sg.Radio('b)Alternativa B','resposta', key = 'letrab1')],
        [sg.Radio('c)Alternativa C','resposta', key = 'letrac1')],
        [sg.Radio('d)Alternativa D','resposta', key = 'letrad1')],
        [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 1', layout =  layout, finalize = True)

def questao2():
        
    #Layout
    sg.theme('reddit')
    layout = [
        [sg.Text('Enunciado',size = (70,3))],
        [sg.Radio('a)Alternativa A','resposta', key = 'letraa2')],
        [sg.Radio('b)Alternativa B','resposta', key = 'letrab2')],
        [sg.Radio('c)Alternativa C','resposta', key = 'letrac2')],
        [sg.Radio('d)Alternativa D','resposta', key = 'letrad2')],
        [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 2', layout =  layout, finalize = True)

def questao3():
        
    #Layout
    sg.theme('reddit')
    layout = [
        [sg.Text('Enunciado',size = (70,3))],
        [sg.Radio('a)Alternativa A','resposta', key = 'letraa3')],
        [sg.Radio('b)Alternativa B','resposta', key = 'letrab3')],
        [sg.Radio('c)Alternativa C','resposta', key = 'letrac3')],
        [sg.Radio('d)Alternativa D','resposta', key = 'letrad3')],
        [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 3', layout =  layout, finalize = True)

def questao4():
        
    #Layout
    sg.theme('reddit')
    layout = [
        [sg.Text('Enunciado',size = (70,3))],
        [sg.Radio('a)Alternativa A','resposta', key = 'letraa4')],
        [sg.Radio('b)Alternativa B','resposta', key = 'letrab4')],
        [sg.Radio('c)Alternativa C','resposta', key = 'letrac4')],
        [sg.Radio('d)Alternativa D','resposta', key = 'letrad4')],
        [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 4', layout =  layout, finalize = True)

def questao5():
        
    #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa5')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab5')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac5')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad5')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 5', layout =  layout, finalize = True)

def questao6():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa6')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab6')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac6')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad6')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 6', layout =  layout, finalize = True)

def questao7():
        
    #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa7')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab7')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac7')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad7')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 7', layout =  layout, finalize = True)

def questao8():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa8')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab8')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac8')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad8')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 8', layout =  layout, finalize = True)

def questao9():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa9')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab9')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac9')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad9')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 9', layout =  layout, finalize = True)

def questao10():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa10')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab10')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac10')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad10')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 10', layout =  layout, finalize = True)

def questao11():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa11')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab11')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac11')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad11')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 11', layout =  layout, finalize = True)

def questao12():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa12')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab12')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac12')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad12')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 12', layout =  layout, finalize = True)



def questao13():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa13')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab13')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac13')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad13')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 13', layout =  layout, finalize = True)

def questao14():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa14')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab14')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac14')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad14')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 14', layout =  layout, finalize = True)

def questao15():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa15')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab15')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac15')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad15')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 15', layout =  layout, finalize = True)

def questao16():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa16')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab16')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac16')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad16')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 16', layout =  layout, finalize = True)

def questao17():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa17')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab17')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac17')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad17')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 17', layout =  layout, finalize = True)

def questao18():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa18')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab18')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac18')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad18')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 18', layout =  layout, finalize = True)

def questao19():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa19')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab19')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac19')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad19')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 19', layout =  layout, finalize = True)

def questao20():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa20')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab20')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac20')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad20')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 20', layout =  layout, finalize = True)

def questao21():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa21')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab21')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac21')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad21')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 21', layout =  layout, finalize = True)

def questao22():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa22')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab22')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac22')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad22')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 22', layout =  layout, finalize = True)

def questao23():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa23')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab23')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac23')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad23')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 23', layout =  layout, finalize = True)

def questao24():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa24')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab24')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac24')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad24')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 24', layout =  layout, finalize = True)

def questao25():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa25')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab25')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac25')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad25')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 25', layout =  layout, finalize = True)

def questao26():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa26')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab26')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac26')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad26')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 26', layout =  layout, finalize = True)

def questao27():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa27')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab27')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac27')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad27')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 27', layout =  layout, finalize = True)

def questao28():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa28')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab28')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac28')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad28')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 28', layout =  layout, finalize = True)

def questao29():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa29')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab29')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac29')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad29')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 29', layout =  layout, finalize = True)

def questao30():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa30')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab30')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac30')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad30')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 30', layout =  layout, finalize = True)

def questao31():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa31')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab31')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac31')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad31')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 31', layout =  layout, finalize = True)

def questao32():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa32')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab32')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac32')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad32')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 32', layout =  layout, finalize = True)

def questao33():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa33')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab33')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac33')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad33')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 33', layout =  layout, finalize = True)

def questao34():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa34')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab34')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac34')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad34')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 34', layout =  layout, finalize = True)

def questao35():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa35')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab35')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac35')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad35')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 35', layout =  layout, finalize = True)

def questao36():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa36')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab36')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac36')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad36')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 36', layout =  layout, finalize = True)

def questao37():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa37')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab37')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac37')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad37')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 37', layout =  layout, finalize = True)

def questao38():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa38')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab38')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac38')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad38')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 38', layout =  layout, finalize = True)

def questao39():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa39')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab39')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac39')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad39')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 39', layout =  layout, finalize = True)

def questao40():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa40')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab40')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac40')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad40')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 40', layout =  layout, finalize = True)

def questao41():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa41')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab41')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac41')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad41')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 41', layout =  layout, finalize = True)

def questao42():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa42')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab42')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac42')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad42')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 42', layout =  layout, finalize = True)

def questao43():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa43')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab43')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac43')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad43')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 43', layout =  layout, finalize = True)

def questao44():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa44')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab44')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac44')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad44')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 44', layout =  layout, finalize = True)

def questao45():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa45')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab45')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac45')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad45')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 45', layout =  layout, finalize = True)


def questao46():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa46')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab46')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac46')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad46')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 46', layout =  layout, finalize = True)

def questao47():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa47')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab47')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac47')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad47')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 47', layout =  layout, finalize = True)

def questao48():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa48')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab48')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac48')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad48')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 48', layout =  layout, finalize = True)

def questao49():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa49')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab49')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac49')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad49')],
            [sg.Button('Próxima')]
        ] 
    return sg.Window('Questão 49', layout =  layout, finalize = True)

def questao50():
        
        #Layout
    sg.theme('reddit')
    layout = [
            [sg.Text('Enunciado',size = (70,3))],
            [sg.Radio('a)Alternativa A','resposta', key = 'letraa50')],
            [sg.Radio('b)Alternativa B','resposta', key = 'letrab50')],
            [sg.Radio('c)Alternativa C','resposta', key = 'letrac50')],
            [sg.Radio('d)Alternativa D','resposta', key = 'letrad50')],
            [sg.Button('Resultado')]
        ] 
    return sg.Window('Questão 50', layout =  layout, finalize = True)

    


#criar as janelas iniciais

janela1, janela2, janela3, janela4, janela5 = questao1(),None, None, None, None
janela6, janela7, janela8, janela9, janela10 = None, None, None, None, None
janela11, janela12, janela13, janela14, janela15 = None, None, None, None, None
janela16, janela17, janela18, janela19, janela20 = None, None, None, None, None
janela21, janela22, janela23, janela24, janela25 = None, None, None, None, None
janela26, janela27, janela28, janela29, janela30 = None, None, None, None, None
janela31, janela32, janela33, janela34, janela35 = None, None, None, None, None
janela36, janela37, janela38, janela39, janela40 = None, None, None, None, None
janela41, janela42, janela43, janela44, janela45 = None, None, None, None, None
janela46, janela47, janela48, janela49, janela50 = None, None, None, None, None

#criar um loop de leitura de eventos 

while True:
    window,event,values = read_all_windows()


    #Quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    if window == janela2 and event == sg.WIN_CLOSED:
        break

    if window == janela3 and event == sg.WIN_CLOSED:
        break

    if window == janela4 and event == sg.WIN_CLOSED:
        break

    if window == janela5 and event == sg.WIN_CLOSED:
        break


    #Quando queremos ir para a próxima janela
    if window == janela1 and event == 'Próxima':
        janela2 == questao2()
        janela1.hide()

    if window == janela2 and event == 'Próxima':
        janela3 == questao3()
        janela2.hide()

    if window == janela3 and event == 'Próxima':
        janela4 == questao4()
        janela3.hide()

    if window == janela4 and event == 'Próxima':
        janela5 == questao5()
        janela4.hide()

    if window == janela5 and event == 'Próxima':
        janela6 == questao6()
        janela5.hide()

    if window == janela6 and event == 'Próxima':
        janela7 == questao7()
        janela6.hide()

    if window == janela7 and event == 'Próxima':
        janela8 == questao8()
        janela7.hide()

    if window == janela8 and event == 'Próxima':
        janela9 == questao9()
        janela8.hide()

    if window == janela9 and event == 'Próxima':
        janela10 == questao10()
        janela9.hide()

    if window == janela10 and event == 'Próxima':
        janela11 == questao11()
        janela10.hide()

    if window == janela11 and event == 'Próxima':
        janela12 == questao12()
        janela11.hide()

    if window == janela12 and event == 'Próxima':
        janela13 == questao13()
        janela12.hide()

    if window == janela13 and event == 'Próxima':
        janela14 == questao14()
        janela13.hide()

    if window == janela14 and event == 'Próxima':
        janela15 == questao15()
        janela14.hide()

    if window == janela15 and event == 'Próxima':
        janela16 == questao16()
        janela15.hide()

    if window == janela16 and event == 'Próxima':
        janela17 == questao17()
        janela16.hide()

    if window == janela17 and event == 'Próxima':
        janela18 == questao18()
        janela17.hide() 

    if window == janela18 and event == 'Próxima':
        janela19 == questao19()
        janela18.hide() 

    if window == janela19 and event == 'Próxima':
        janela20 == questao20()
        janela19.hide() 

    if window == janela20 and event == 'Próxima':
        janela21 == questao21()
        janela20.hide() 

    if window == janela21 and event == 'Próxima':
        janela22 == questao22()
        janela21.hide() 

    if window == janela22 and event == 'Próxima':
        janela23 == questao23()
        janela22.hide() 

    if window == janela23 and event == 'Próxima':
        janela24 == questao24()
        janela23.hide() 

    if window == janela24 and event == 'Próxima':
        janela25 == questao25()
        janela24.hide() 

    if window == janela25 and event == 'Próxima':
        janela26 == questao26()
        janela25.hide() 

    if window == janela26 and event == 'Próxima':
        janela27 == questao27()
        janela26.hide() 

    if window == janela27 and event == 'Próxima':
        janela28 == questao28()
        janela27.hide() 

    if window == janela28 and event == 'Próxima':
        janela29 == questao29()
        janela28.hide() 

    if window == janela29 and event == 'Próxima':
        janela30 == questao30()
        janela29.hide() 

    if window == janela30 and event == 'Próxima':
        janela31 == questao31()
        janela30.hide() 

    if window == janela31 and event == 'Próxima':
        janela32 == questao32()
        janela31.hide() 

    if window == janela32 and event == 'Próxima':
        janela33 == questao33()
        janela32.hide() 

    if window == janela33 and event == 'Próxima':
        janela34 == questao34()
        janela33.hide() 

    if window == janela34 and event == 'Próxima':
        janela35 == questao35()
        janela34.hide() 

    if window == janela35 and event == 'Próxima':
        janela36 == questao36()
        janela35.hide() 

    if window == janela36 and event == 'Próxima':
        janela37 == questao37()
        janela36.hide() 

    if window == janela37 and event == 'Próxima':
        janela38 == questao38()
        janela37.hide() 

    if window == janela38 and event == 'Próxima':
        janela39 == questao39()
        janela38.hide() 

    if window == janela39 and event == 'Próxima':
        janela40 == questao40()
        janela39.hide() 

    if window == janela40 and event == 'Próxima':
        janela41 == questao41()
        janela40.hide() 

    if window == janela41 and event == 'Próxima':
        janela42 == questao42()
        janela41.hide() 

    if window == janela42 and event == 'Próxima':
        janela43 == questao43()
        janela42.hide() 

    if window == janela43 and event == 'Próxima':
        janela44 == questao44()
        janela43.hide()

    if window == janela44 and event == 'Próxima':
        janela45 == questao45()
        janela44.hide() 

    if window == janela45 and event == 'Próxima':
        janela46 == questao46()
        janela45.hide() 

    if window == janela46 and event == 'Próxima':
        janela47 == questao47()
        janela46.hide() 

    if window == janela47 and event == 'Próxima':
        janela48 == questao48()
        janela47.hide() 

    if window == janela48 and event == 'Próxima':
        janela49 == questao49()
        janela48.hide() 

    if window == janela49 and event == 'Próxima':
        janela50 == questao50()
        janela49.hide() 
                                                                                                                
       
#lógica do que deve acontecer ao clicar nos botoes
def Iniciar(self):
    pontuacao = 0
    a1 = self.values['letraa1']
    b1 = self.values['letrab1']
    c1 = self.values['letrac1']
    d1 = self.values['letrad1']

    if d1 == True:
        pontuacao += 1

    a2 = self.values['letraa2']
    b2 = self.values['letrab2']
    c2 = self.values['letrac2']
    d2 = self.values['letrad2']

    if d2 == True:
        pontuacao += 1 

    a3 = self.values['letraa3']
    b3 = self.values['letrab3']
    c3 = self.values['letrac3']
    d3 = self.values['letrad3'] 

    if d3 == True:
        pontuacao += 1

    a4 = self.values['letraa4']
    b4 = self.values['letrab4']
    c4 = self.values['letrac4']
    d4 = self.values['letrad4'] 

    if d4 == True:
        pontuacao += 1

    a5 = self.values['letraa5']
    b5 = self.values['letrab5']
    c5 = self.values['letrac5']
    d5 = self.values['letrad5']

    if d5 == True:
        pontuacao += 1 

    a6 = self.values['letraa6']
    b6 = self.values['letrab6']
    c6 = self.values['letrac6']
    d6 = self.values['letrad6']

    if d6 == True:
        pontuacao += 1 

    a7 = self.values['letraa7']
    b7 = self.values['letrab7']
    c7 = self.values['letrac7']
    d7 = self.values['letrad7']

    if d7 == True:
        pontuacao += 1 

    a8 = self.values['letraa8']
    b8 = self.values['letrab8']
    c8 = self.values['letrac8']
    d8 = self.values['letrad8']

    if d8 == True:
        pontuacao += 1 

    a9 = self.values['letraa9']
    b9 = self.values['letrab9']
    c9 = self.values['letrac9']
    d9 = self.values['letrad9']

    if d9 == True:
        pontuacao += 1 

    a10 = self.values['letraa10']
    b10 = self.values['letrab10']
    c10 = self.values['letrac10']
    d10 = self.values['letrad10']

    if d10 == True:
        pontuacao += 1

    a11 = self.values['letraa11']
    b11 = self.values['letrab11']        
    c11 = self.values['letrac11']
    d11 = self.values['letrad11']

    if d11 == True:
        pontuacao += 1


    a12 = self.values['letraa12']
    b12 = self.values['letrab12']
    c12 = self.values['letrac12']
    d12 = self.values['letrad12']

    if d12 == True:
        pontuacao += 1 

    a13 = self.values['letraa13']
    b13 = self.values['letrab13']
    c13 = self.values['letrac13']
    d13 = self.values['letrad13']

    if d13 == True:
        pontuacao += 1 

    a14 = self.values['letraa14']
    b14 = self.values['letrab14']
    c14 = self.values['letrac14']
    d14 = self.values['letrad14']

    if d14 == True:
        pontuacao += 1 

    a15 = self.values['letraa15']
    b15 = self.values['letrab15']
    c15 = self.values['letrac15']
    d15 = self.values['letrad15']

    if d15 == True:
        pontuacao += 1 

    a16 = self.values['letraa16']
    b16 = self.values['letrab16']
    c16 = self.values['letrac16']
    d16 = self.values['letrad16']

    if d16 == True:
        pontuacao += 1 

    a17 = self.values['letraa17']
    b17 = self.values['letrab17']
    c17 = self.values['letrac17']
    d17 = self.values['letrad17']

    if d17 == True:
        pontuacao += 1 

    a18 = self.values['letraa18']
    b18 = self.values['letrab18']
    c18 = self.values['letrac18']
    d18 = self.values['letrad18']

    if d18 == True:
        pontuacao += 1 

    a19 = self.values['letraa19']
    b19 = self.values['letrab19']
    c19 = self.values['letrac19']
    d19 = self.values['letrad19']
        
    if d19 == True:
        pontuacao += 1

    a20 = self.values['letraa20']
    b20 = self.values['letrab20']
    c20 = self.values['letrac20']
    d20 = self.values['letrad20']

    if d20 == True:
        pontuacao += 1 

    a21 = self.values['letraa21']
    b21 = self.values['letrab21']
    c21 = self.values['letrac21']
    d21 = self.values['letrad21']

    if d21 == True:
        pontuacao += 1 

    a22 = self.values['letraa22']
    b22 = self.values['letrab22']
    c22 = self.values['letrac22']
    d22 = self.values['letrad22']

    if d22 == True:
        pontuacao += 1 

    a23 = self.values['letraa23']
    b23 = self.values['letrab23']
    c23 = self.values['letrac23']
    d23 = self.values['letrad23']

    if d23 == True:
        pontuacao += 1 

    a24 = self.values['letraa24']
    b24 = self.values['letrab24']
    c24 = self.values['letrac24']
    d24 = self.values['letrad24']

    if d24 == True:
        pontuacao += 1 

    a25 = self.values['letraa25']
    b25 = self.values['letrab25']
    c25 = self.values['letrac25']
    d25 = self.values['letrad25']

    if d25 == True:
        pontuacao += 1 

    a26 = self.values['letraa26']
    b26 = self.values['letrab26']
    c26 = self.values['letrac26']
    d26 = self.values['letrad26']

    if d26 == True:
        pontuacao += 1 

    a27 = self.values['letraa27']
    b27 = self.values['letrab27']
    c27 = self.values['letrac27']
    d27 = self.values['letrad27']

    if d27 == True:
        pontuacao += 1 

    a28 = self.values['letraa28']
    b28 = self.values['letrab28']
    c28 = self.values['letrac28']
    d28 = self.values['letrad28']

    if d28 == True:
        pontuacao += 1 

    a29 = self.values['letraa29']
    b29 = self.values['letrab29']
    c29 = self.values['letrac29']
    d29 = self.values['letrad29']

    if d29 == True:
        pontuacao += 1 

    a30 = self.values['letraa30']
    b30 = self.values['letrab30']
    c30 = self.values['letrac30']
    d30 = self.values['letrad30']

    if d30 == True:
        pontuacao += 1 

    a31 = self.values['letraa31']
    b31 = self.values['letrab31']
    c31 = self.values['letrac31']
    d31 = self.values['letrad31']

    if d31 == True:
        pontuacao += 1 

    a32 = self.values['letraa32']
    b32 = self.values['letrab32']
    c32 = self.values['letrac32']
    d32 = self.values['letrad32']

    if d32 == True:
        pontuacao += 1 

    a33 = self.values['letraa33']
    b33 = self.values['letrab33']
    c33 = self.values['letrac33']
    d33 = self.values['letrad33']

    if d33 == True:
        pontuacao += 1 

    a34 = self.values['letraa34']
    b34 = self.values['letrab34']
    c34 = self.values['letrac34']
    d34 = self.values['letrad34']

    if d34 == True:
        pontuacao += 1 

    a35 = self.values['letraa35']
    b35 = self.values['letrab35']
    c35 = self.values['letrac35']
    d35 = self.values['letrad35']

    if d35 == True:
        pontuacao += 1 

    a36 = self.values['letraa36']
    b36 = self.values['letrab36']
    c36 = self.values['letrac36']
    d36 = self.values['letrad36']

    if d36 == True:
        pontuacao += 1 

    a37 = self.values['letraa37']
    b37 = self.values['letrab37']
    c37 = self.values['letrac37']
    d37 = self.values['letrad37']

    if d37 == True:
        pontuacao += 1 

    a38 = self.values['letraa38']
    b38 = self.values['letrab38']
    c38 = self.values['letrac38']
    d38 = self.values['letrad38']

    if d38 == True:
        pontuacao += 1 

    a39 = self.values['letraa39']
    b39 = self.values['letrab39']
    c39 = self.values['letrac39']
    d39 = self.values['letrad39']

    if d39 == True:
        pontuacao += 1 

    a40 = self.values['letraa40']
    b40 = self.values['letrab40']
    c40 = self.values['letrac40']
    d40 = self.values['letrad40']

    if d40 == True:
        pontuacao += 1 

    a41 = self.values['letraa41']
    b41 = self.values['letrab41']
    c41 = self.values['letrac41']
    d41 = self.values['letrad41']

    if d41 == True:
        pontuacao += 1 

    a42 = self.values['letraa42']
    b42 = self.values['letrab42']
    c42 = self.values['letrac42']
    d42 = self.values['letrad42']

    if d42 == True:
        pontuacao += 1 

    a43 = self.values['letraa43']
    b43 = self.values['letrab43']
    c43 = self.values['letrac43']
    d43 = self.values['letrad43']

    if d43 == True:
        pontuacao += 1 

    a44 = self.values['letraa44']
    b44 = self.values['letrab44']
    c44 = self.values['letrac44']
    d44 = self.values['letrad44']

    if d44 == True:
        pontuacao += 1 

    a45 = self.values['letraa45']
    b45 = self.values['letrab45']
    c45 = self.values['letrac45']
    d45 = self.values['letrad45']

    if d45 == True:
        pontuacao += 1 

    a46 = self.values['letraa46']
    b46 = self.values['letrab46']
    c46 = self.values['letrac46']
    d46 = self.values['letrad46']

    if d46 == True:
        pontuacao += 1 

    a47 = self.values['letraa47']
    b47 = self.values['letrab47']
    c47 = self.values['letrac47']
    d47 = self.values['letrad47']

    if d47 == True:
        pontuacao += 1 

    a48 = self.values['letraa48']
    b48 = self.values['letrab48']
    c48 = self.values['letrac48']
    d48 = self.values['letrad48']

    if d48 == True:
        pontuacao += 1 

    a49 = self.values['letraa49']
    b49 = self.values['letrab49']
    c49 = self.values['letrac49']
    d49 = self.values['letrad49']

    if d49 == True:
        pontuacao += 1 

    a50 = self.values['letraa50']
    b50 = self.values['letrab50']
    c50 = self.values['letrac50']
    d50 = self.values['letrad50']

    if d50 == True:
        pontuacao += 1   

