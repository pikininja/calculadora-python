print("Calculadora Simples em Python")
print("Digite 'sair' a qualquer momento para encerrar.\n")

while True:
    num1 = input("Digite o primeiro número: ")
    if num1.lower() == 'sair':
        break

    num2 = input("Digite o segundo número: ")
    if num2.lower() == 'sair':
        break

    operador = input("Escolha a operação (+, -, *, /): ")
    if operador.lower() == 'sair':
        break

    try:
        num1 = float(num1)
        num2 = float(num2)

        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                print("Erro: divisão por zero!")
                continue
            resultado = num1 / num2
        else:
            print("Operador inválido.")
            continue

        print(f"Resultado: {resultado}\n")

    except ValueError:
        print("Entrada inválida. Use apenas números.\n")