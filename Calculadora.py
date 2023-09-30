print('Suas opções de Operadores são: +, -, /, * e **')
print('+ para fazer uma conta de adição')
print('- para fazer uma conta de subtração')
print('* para fazer uma conta de multiplicação.')
print('/ para fazer uma conta de divisão.')
print('** para fazer uma conta de potenciação.')

def calcular_equacao(equacao):
    try:
        # Validar a entrada do usuário
        if equacao not in ["Mais", "+", "mais", "Menos", "-", "menos", "Divisão", "/", "divisão", "Multiplicação", "*", "multiplicação", "Exponenciação", "**", "exponenciação"]:
            raise ValueError("Opção inválida")

        # Obter os números da entrada do usuário
        n1 = float(input("Qual seu primeiro número?"))
        n2 = float(input("Qual seu segundo número?"))

        # Verificar se o denominador é zero (divisão por zero)
        if equacao in ["Divisão", "/", "divisão"] and n2 == 0:
            raise ValueError("Erro: Divisão por zero")

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
    except ValueError as e:
        # Tratar a exceção e imprimir a mensagem de erro
        return str(e)

equacao = input("Qual sua Operação? ")
resultado = calcular_equacao(equacao)

if resultado == "Opção inválida" or resultado == "Erro: Divisão por zero":
    print(resultado)
else:
    print("O resultado é", resultado)
