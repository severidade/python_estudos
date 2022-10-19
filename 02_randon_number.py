import random

random_number = random.randint(1, 3)  # escolhe um número aleatório entre 1 e 3
guess = ""

while guess != random_number:  # enquanto não adivinhar o número
    guess = int(input("Qual o palpite? "))
print("O número sorteado era: ", guess)
