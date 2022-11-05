#2. Faça um programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.

def escreva(txt):
    tam = len(txt) +4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


escreva('Olá, Mundo!')
escreva('Gustavo Guanabara!')
escreva('Curso de Python no YouTube!')
escreva('CeV!')
