numeroSec = '17'

while True:
    numeroAdv = input('Adivine el numero secreto o escriba "EXIT" para salir: \n')
    if numeroSec == numeroAdv:
        print('Has adivinado el numero.')
        break
    elif numeroAdv == 'EXIT':
        print('Has salido.')
        break
    