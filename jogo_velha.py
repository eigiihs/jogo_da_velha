tabuleiro = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

jogadas = 1
jogador = 'X'
play = True
posicoes_validas = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}

def show_tabuleiro():
    for i in range(3):
        print(' | '.join(tabuleiro[i]))
        if i < 2:
            print('-' * 9)

def reset_tabuleiro():
    return [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
    ]

def verify_vencedor():
    # verifica as linhas
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2]:
            return True

    # verifica as colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna]:
            return True

    # verifica as diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] or  \
        tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        return True

    return False 

def realizar_jogada(position, jogador):
    for linha in range(3):
                for coluna in range(3):
                    if tabuleiro[linha][coluna] == position:
                        tabuleiro[linha][coluna] = jogador
                        return True
    return False

def menu():
    global play
    global jogadas
    global tabuleiro
    print(f'\n---- MENU INICIAL ----')
    print(f'1 - Jogar novamente')
    print(f'2 - Finalizar')
    print(f'-----------------------')

    option = int(input('Informe o que deseja fazer: '))
    if option == 2:
        play = False
    else: 
        jogadas = 1
        tabuleiro = reset_tabuleiro()
    
while play: 

    while jogadas <= 9:
        print(f'\nRodada: {jogadas}')
        show_tabuleiro()

        position = input(f'{jogador} - Insira a posição: ')
        if position not in posicoes_validas:
            print('-Posição não encontrada! Digite novamente! -')
         
        if realizar_jogada(position, jogador):
            if verify_vencedor():
                show_tabuleiro()
                print(f'\n{jogador} Venceu!!')
                menu()
                break 

            if jogadas == 9:
                show_tabuleiro()
                print(f'Deu Velha!!')
                menu()
                break

            jogadas += 1
            jogador = 'O' if jogador == 'X' else 'X' 