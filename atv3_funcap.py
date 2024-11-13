def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
 

numero = int(input("Digite um numero: "))
resultado = par_ou_impar(numero)
print(f"O seu número {numero} é {resultado}.")
    