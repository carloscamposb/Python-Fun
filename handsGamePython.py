import random

escolha = int(input('Escolha entre 1-pedra 2-papel e 3-tesoura: '))

if escolha == 1:
    print('Você escolheu pedra  ✊')
elif escolha == 2:
    print('Você escolheu papel  🖐')
elif escolha == 3:
    print('Você escolheu tesoura ✌')
else:
    print('Escolha incorreta')

sorte = random.randint(1, 3)

if sorte == 1:
    print('O computador escolheu pedra. ✊')
elif sorte == 2:
    print('O computador escolheu papel. 🖐' )
elif sorte == 3:
    print('O computador escolheu tesoura. ✌')

if escolha == sorte:
    print('Empate! Tente novamente.')
elif escolha == 1 and sorte == 2:
    print('Papel embrulha pedra. Você perdeu! 🖐>✊')
elif escolha == 1 and sorte == 3:
    print('Pedra quebra tesoura. Você ganhou! ✊> ✌')
elif escolha == 2 and sorte == 1:
    print('Papel embrulha pedra. Você ganhou! 🖐>✊')
elif escolha == 2 and sorte == 3:
    print('Tesoura corta papel. Você perdeu!  ✌>🖐')
elif escolha == 3 and sorte == 1:
    print('Pedra quebra tesoura. Você perdeu! ✊>✌')
elif escolha == 3 and sorte == 2:
    print('Tesoura corta papel. Você ganhou!  ✌>🖐')
else:
    print('Escolha incorreta')
