import random

numero_secreto = random.randint(1, 10)
tentativas = 0
print("################# JOGO ADIVINHAÇÃO #################\n")

print("Olá! Vamos jogar um jogo de adivinhação.")
print("Estou pensando em um número entre 1 e 10. Tente adivinhar!")

while tentativas < 3:
    tentativa = int(input("Qual é o número? "))
    tentativas += 1

    if tentativa == numero_secreto:
        print(" *** Parabéns! Você acertou em", tentativas, "tentativa(s) *** ")
        break
    elif tentativa < numero_secreto:
        print("O número é maior. Tente novamente.")
    else:
        print("O número é menor. Tente novamente.")

if tentativas == 3:
    print(" --- Suas tentativas acabaram. O número secreto era", numero_secreto," ---")