categorias = ['Aquecimento', 'Superiores', 'Inferiores', 'Costas']
aquecimento = [
    ['Ex. de aquecimento 1', 'descrição aquecimento 1'],
    ['Ex. de aquecimento 2', 'descrição aquecimento 2'],
    ['Ex. de aquecimento 3', 'descrição aquecimento 3']
]
superiores = [
    ['Ex. superior 1', 'descrição superior 1'],
    ['Ex. superior 2', 'descrição superior 2'],
    ['Ex. superior 3', 'descrição superior 3']
]
inferiores = [
    ['Ex. inferior 1', 'descrição inferior 1'],
    ['Ex. inferior 2', 'descrição inferior 2'],
    ['Ex. inferior 3', 'descrição inferior 3']
]
costas = [
    ['Ex. costa 1', 'descrição costa 1'],
    ['Ex. costa 2', 'descrição costa 2'],
    ['Ex. costa 3', 'descrição costa 3']
]

def calcular_imc():
    while True:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros (ex: 1.70): "))
        if peso == 0 or altura == 0:
            print("Insira um valor válido")
        else:
            imc = peso / (altura * altura)
            print(f"Seu IMC é {imc:.2f}.")
            print('')
            break

def categoria(x):
    print(f'{categorias[x-1]} - Lista de exercícios')
    if x == 1:
        for i in range(0, 3):
            print(f'{i + 1} - {aquecimento[i][0]}')
    elif x == 2:
        for i in range(0, 3):
            print(f'{i + 1} - {superiores[i][0]}')
    elif x == 3:
        for i in range(0, 3):
            print(f'{i + 1} - {inferiores[i][0]}')
    elif x == 4:
        for i in range(0, 3):
            print(f'{i + 1} - {costas[i][0]}')
    print('')
    opcao = int (input('Escolha um exercício para acessar: '))
    exercicio(x, opcao-1)

def exercicio(x, y):
    if x == 1:
        print(aquecimento[y][1])
    elif x == 2:
        print(superiores[y][1])
    elif x == 3:
        print(inferiores[y][1])
    elif x == 4:
        print(costas[y][1])
    print('')
    opcao = input('Digite X para fechar: ')
    if opcao.lower() == 'x':
        print('')
        menu()

def menu():
    print('=========== MENU ===========')
    print('1- Exercícios de aquecimento')
    print('2- Superiores')
    print('3- Inferiores')
    print('4- Costas')
    print(' ')
    opcao = int (input('Escolha uma aba para acessar: '))
    categoria(opcao)

calcular_imc()
menu()