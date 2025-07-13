"""

Recebe dois dados vindos do usuários e os concatene em uma única string.

"""

def concatenar_dados_usuario(dado1, dado2):
    """
    
    Concatena em uma única string dois dados vindos do usuário.

    """
    return dado1 + " " + dado2


def coletar_dados_usuario():
    """
    
    Recebe dois dados informandos pelo usuário através do terminal.

    """
    primeiro_dado = input("Informe o primeiro dado: ")
    segundo_dado = input("Informe o segundo dado: ")
    
    return (primeiro_dado, segundo_dado)


primeiro_dado, segundo_dado = coletar_dados_usuario()
resultado = concatenar_dados_usuario(primeiro_dado, segundo_dado)
print(F"As informações concatenadas foram: ", resultado)
