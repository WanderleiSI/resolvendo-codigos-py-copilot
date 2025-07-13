"""

Solicite uma string e em seguida um número inteiro como entrada. Em seguida, retorne a string
repetida o número de vezes informado.

"""

def solicitar_string():
    """

    Coleta a string do usuário.
    
    """
    
    string = input("Informe uma string: ")
    return string


def solicitar_numero():
    """

    Coleta o número do usuário
    
    """

    while True:
        numero = input("Informe um número inteiro: ")

        if numero.isdigit():
            return int(numero)
        else:
            print("Entrada inválida. Por favor, informe um número inteiro.")


def repetir_texto(texto, vezes):
    """

    Repete a string o número de vezes especificado.

    """
    return texto * vezes


texto = solicitar_string()
numero_para_repetir = solicitar_numero()
resultado = repetir_texto(texto, numero_para_repetir)
print(f"String {texto} repetida {numero_para_repetir}: {resultado}")