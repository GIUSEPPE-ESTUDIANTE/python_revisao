
def verificar_palindromo(palavra):
    """
    Verifica se uma palavra é um palíndromo.
    :param palavra: Palavra a ser verificada
    :return: True se a palavra for um palíndromo, False caso contrário
    """
    
    palavra = palavra.replace(" ", "").lower()
    
    return palavra == palavra[::-1]


palavra = input("Digite uma palavra ou frase: ")
if verificar_palindromo(palavra):
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')

