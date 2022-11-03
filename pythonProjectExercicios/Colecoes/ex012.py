#12. Crie um programa onde o usuário digita uma expressão qualquer que usa parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = input('Digite a expressão: ')
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')
