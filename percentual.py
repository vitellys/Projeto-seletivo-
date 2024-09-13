#função para calcular o percentual dos estados
def calcular_percentuais(faturamento):
#calcula o valor total de faturamento
    total = sum(faturamento.values())
    
#armazena os percentuais
    percentuais = {}
    
#calcula para cada estados
    for estado, valor in faturamento.items():
        percentuais[estado] = (valor / total) * 100
    
    return percentuais

#função principal para chamar a função de calcular os percentuais
def main():
#dados de faturamento
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
#calcula e imprime os resultados
    percentuais = calcular_percentuais(faturamento)
    print("Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

#esta linha garante que o código abaixo só seja executado se o script for executado diretamente, e não quando importado como um módulo em outro script.
if __name__ == "__main__":
    main()
