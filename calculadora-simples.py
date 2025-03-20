
# Definir algumas funções como: somar, subtrair, multiplicar e divisão dos 2 números
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

# Funções da calculadora
def calculadora():
    print("Bem-vindo à Calculadora!")
    print("Operações disponíveis:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")

# Solicitar operação para o usuário
    operacao = input("Escolha a operação (1/2/3/4): ")

# Verificar se opção está válida 
    if operacao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == '1':
            print(f"Resultado: {soma(num1, num2)}")
        elif operacao == '2':
            print(f"Resultado: {subtracao(num1, num2)}")
        elif operacao == '3':
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif operacao == '4':
            print(f"Resultado: {divisao(num1, num2)}")
    else:
        print("Operação inválida!")
        
# Rodar o script diretamente 
if __name__ == "__main__":
    calculadora()