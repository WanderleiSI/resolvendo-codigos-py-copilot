"""
Solicitar dois números inteiros ao usuário e realizar operações matemáticas simples entre eles.
"""

def coletar_numeros():
    """
    Coleta dois números inteiros do usuário.
    """

    while True:
        try:
            numero1 = int(input("Digite o primeiro número: "))
            numero2 = int(input("Digite o segundo número: "))
            return (numero1, numero2)
        except ValueError:
            print("Por favor, digite dois números inteiros válidos.")


def escolher_operacao():
    """
    Solicita ao usuário que escolha uma operação matemática.
    """
    
    operacoes = {
        '1': 'Soma',
        '2': 'Subtração',
        '3': 'Multiplicação',
        '4': 'Divisão'
    }
    
    print("Escolha uma operação:")
    for chave, valor in operacoes.items():
        print(f"{chave}: {valor}")
    
    while True:
        escolha = input("Digite o número da operação desejada: ")
        if escolha in operacoes:
            return escolha
        else:
            print("Opção inválida. Tente novamente.")


def realizar_operacao(numero1, numero2, operacao):
    """
    Realiza a operação matemática escolhida entre os dois números.
    """
    
    resultado = {
        '1': numero1 + numero2,  # Soma
        '2': abs(numero1 - numero2),  # Subtração
        '3': numero1 * numero2,  # Multiplicação
        '4': numero1 / numero2 if numero2 != 0 else "Erro: Divisão por zero não é permitida."  # Divisão
    }

    return resultado.get(operacao, "Operação inválida.")


numero1, numero2 = coletar_numeros()
operacao = escolher_operacao()
resultado = realizar_operacao(numero1, numero2, operacao)
print(f"O resultado da operação escolhida é: {resultado}")