import random

def adivinhar():
    tentativas = 0;

    print("Bem vindo ao jogo de adivinhação!")
    print("O objetivo é adivinhar um número entre 1 e 200")

    number = random.randint(1,200)
    
    while True:
        n = int(input("Digite um número: "))
        if(n != number):
            tentativas+=1;
            if(n < number):
                print("Tente mais alto!")
            else:
                print("Tente mais baixo!")
        if(n == number):
            print("Parabeeeens!!!!")
            print("Você acertou!!!!!!")
            print("Número certo -> " + str(number))
            print(f"Você tentou {tentativas} vezes")
            break;
        
adivinhar();

