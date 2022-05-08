# contagem = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
import time

contagem = (
    "Zero", "Um", "Dois", "três", "quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze",
    "Quatorze",
    "Quinze", "Dezesseis",
    "Dezessete", "Dezoito", "Dezenove", "Vinte")
resp = ' '
while True:
    pergunta = int(input("Digite um numero de 0 a 20: "))
    if pergunta > 20:
        print("Numero invalido tente novamente!")
    if pergunta <= 20:
        print(f"O Numero digitado é {contagem[pergunta]} ")
        continuar = str(input("Você quer continuar? [S/N]: ")).strip().upper()[0]
        if continuar in "S":
            pergunta = int(input("Digite um numero de 0 a 20: "))
            print(f"O Numero digitado é {contagem[pergunta]} ")
        if continuar in "N":
            print("Finalizando...")
            time.sleep(1)
            break
        else:
            if continuar not in "S" or "N":
                continuar = str(input("Você quer continuar? [S/N]: ")).strip().upper()[0]
