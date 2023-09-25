def calcular_equacao(equacao):
    # Validar a entrada do usuário
    if equacao not in ["Mais", "+", "mais", "Menos", "-", "menos", "Divisão", "/", "divisão", "Multiplicação", "*", "multiplicação", "Exponenciação", "**"]:
        raise ValueError("Opção inválida")

    # Obter os números da entrada do usuário
    n1 = float(input("Qual seu primeiro numero?"))
    n2 = float(input("Qual seu segundo numero?"))

    # Calcular o resultado da equação
    if equacao == "Mais" or equacao == "+" or equacao == "mais":
        total = n1 + n2
    elif equacao == "Menos" or equacao == "-" or equacao == "menos":
        total = n1 - n2
    elif equacao == "Divisão" or equacao == "/" or equacao == "divisão":
        total = n1 / n2
    elif equacao == "Multiplicação" or equacao == "*" or equacao == "multiplicação":
        total = n1 * n2
    elif equacao == "Exponenciação" or equacao == "**":
        total = n1 ** n2

    # Retornar o resultado
    return total


equacao = input("Qual sua equação? ")
resultado = calcular_equacao(equacao)
print("O resultado é", resultado)
