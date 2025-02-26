tabuleiro = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

jogadas = 1
jogador = 'X'
play = True

def show_tabuleiro():
    for i in range(3):
        print(tabuleiro[i])

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

def menu():
    global play
    global jogadas
    global tabuleiro
    print(f'---- MENU INICIAL ----')
    print(f'1 - Jogar novamente')
    print(f'2 - Finalizar')
    print(f'-----------------------')

    option = int(input('Informe o que deseja fazer: '))
    if option == 2:
        play = False
    else: 
        jogadas = 1
        tabuleiro = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
    
while play: 

    while jogadas < 10:
        print(f'Rodada: {jogadas}')

        show_tabuleiro()

        position = input(f'{jogador} - Insira a posição: ')
        if position != 'a' and position != 'b' and position != 'c' and position != 'd' and position != 'e' and \
            position != 'f' and position != 'g' and position != 'h' and position != 'i':
            print('-Posição não encontrada!-')
            print('-Digite novamente!-')
        else: 
            jogada_realizada = False
            for linha in range(3):
                for coluna in range(3):
                    if tabuleiro[linha][coluna] == position:
                        tabuleiro[linha][coluna] = jogador
                        jogada_realizada = True
        
            if verify_vencedor():
                show_tabuleiro()
                print(f'{jogador} Venceu!!')
                menu()
                break 

            if jogada_realizada == True:
                jogadas += 1
                jogador = 'O' if jogador == 'X' else 'X' 
