# Fatores de conversão para metros
fatores = {
    "quilômetro": 1e3,
    "metro": 1,
    "centímetro": 1e-2,
    "milímetro": 1e-3,
    "micrômetro": 1e-6,
    "nanômetro": 1e-9,
    "milha": 1609.34,
    "jarda": 0.9144,
    "pé": 0.3048,
    "polegada": 0.0254
}

def converter_unidades(valor, unidade_origem, unidade_destino):

    # Verifica se as unidades fornecidas são válidas
    if unidade_origem not in fatores or unidade_destino not in fatores:
        return "Unidade não reconhecida."

    # Converte o valor para metros

    valor_em_metros = valor * fatores[unidade_origem]
    
    # Converte o valor de metros para a unidade de destino
    valor_convertido = valor_em_metros / fatores[unidade_destino]

    return valor_convertido

def main():
    print("Bem-vindo ao Conversor de Unidades de Comprimento!")
    print("Unidades disponíveis: quilômetro, metro, centímetro, milímetro, micrômetro, nanômetro, milha, jarda, pé, polegada")

    # Solicita entrada do usuário
    valor = float(input("Digite o valor a ser convertido: "))
    unidade_origem = input("Digite a unidade de origem: ").lower()
    unidade_destino = input("Digite a unidade de destino: ").lower()

    # Realiza a conversão
    resultado = converter_unidades(valor, unidade_origem, unidade_destino)

    # Exibe o resultado ou uma mensagem de erro
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"{valor} {unidade_origem} é igual a {resultado} {unidade_destino}.")

if __name__ == "__main__":
    main()