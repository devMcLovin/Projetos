from random import randint
from time import sleep

num_pc = randint(0, 10)
pontos = 0
chances = 3
linha = lambda: '=' * 30
continuar = 's'

while True:
        try:
            if chances < 3:
                continuar = str(input('Quer continuar [s/n]')).upper()
                print(linha())
            if continuar == 'N':
                break
            if chances == 3:
                jogar = str(input('Ei, vamos jogar [s /n]?: ')).upper()
                print(linha())
            if jogar == 'N':
                break
            elif jogar.isnumeric() or continuar.isnumeric() :
                while continuar not in 'SN':
                    print('Digite apenas "s" ou "n".')
                    sleep(2)
                    continuar = str(input('Quer continuar [s/n]')).upper()
                    print(linha())
                if continuar == 'N':
                        break
            if jogar or continuar == 's':
                try:
                    print('Estou pensando em um numero de 0 a 10...')
                    sleep(2)
                    print('pronto!!!')
                    print(linha())
                    num_user = int(input(f'Voçê tem {chances} chances. \nEm qual numero eu pensei de 0 a 10?  '))
                    if num_user == num_pc:
                        chances -= 1
                        pontos += 100
                        print(f'Boooaa!! voçê somou {pontos} pontos')
                        print(linha())
                    else:
                        chances -= 1
                        if chances == 0:
                            print('Voçê errou, Suas chances acabaram.')
                            print(linha())
                            break
                        print(f'voçê errou, voçê ainda tem {chances} chances')
                        print(linha())
                except ValueError:
                    print('Digite apenas neros de 0 a 10')
                    sleep(2)
        except ValueError:
             print('Digite apenas letras')
             sleep(2)
sleep(2)
print(f'Sua pontuação foi de {pontos} pontos')
print('Volte sempre!!!')
