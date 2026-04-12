while True:

    print('\n~~~~ CALCULADORA PYTHON ~~~~')
    num1 = float(input('Digite o 1º número: '))
    num2 = float(input('Digite o 2º número: '))
    operação = input('Qual operação deseja? [ +, -, *, / ] :')

    if operação == '+':
        resposta = num1 + num2
        print(f'{num1} + {num2} = {resposta}')
    elif operação == '-':
        resposta = num1 - num2
        print(f'{num1} - {num2} = {resposta}')
    elif operação == '*':
        resposta = num1 * num2
        print(f'{num1} X {num2} = {resposta}')
    elif operação == '/':
        if num2 == 0:
            print('Error: divisão por zero[0]')
            continue
        resposta = num1 / num2
        print(f'{num1} / {num2} = {resposta}')
    else:
        print('Opção inválida! Tente novamente.')

    sair = str(input('Deseja sair? [S/N]: ')).strip().upper()[0]
    if sair == 'S':
        print('~~' * 20)
        print('Obrigado. Volte sempre!')
        break




