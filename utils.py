def calculaNotaDoQuiz(respostas, gabarito):
    pontuacao = 0
    for resposta in gabarito:
        if respostas[resposta]:
            pontuacao += 1
    
    return pontuacao

if __name__ == '__main__':
    respostas = {'a1': True, 'b1': False, 'c1': False, 'd1': False, 'a2': False, 'b2': False, 'c2': False, 'd2': False}    
    gabarito = ['a1', 'c2']
    calculaNotaDoQuiz(respostas, gabarito)
