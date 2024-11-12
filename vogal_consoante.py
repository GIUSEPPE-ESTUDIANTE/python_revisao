letra = input("Digite uma letra: ").lower().upper()

if letra in "aeiou":
    print("A letra é uma vogal.")
elif letra.isalpha():
    print("A letra é uma consoante.")
else:
    print("Caractere inválido.")
    