import json  #biblioteca para manipular arquivos JSON
import os    #biblioteca para interações com o sistema de arquivos, auxiliando o usuário a encontrar o arquivo com facilidade

def carregar_dados(nome_arquivo):
#função para carregar os dados
#verifica se o arquivo existe no diretório
    if not os.path.isfile(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' não encontrado no diretório atual.")
        print("Forneça o caminho correto e cheque se o arquivo está no diretório atual.")
        return []
#retorna se o arquivo existe ou não, mas só é necessário caso tenha importado a biblioteca OS

    try:
        with open(nome_arquivo, 'r') as file:
            dados = json.load(file) 
            
#carrega os dados do arquivo JSON

#verifica se os dados carregados são uma lista

        if not isinstance(dados, list):
            print("Formato do JSON não esperado.")
            print("O JSON deve ser uma lista de objetos com campos 'dia' e 'valor'.")
            return []
#retorna caso o formato da lista fornecida não seja o esperado. 

#ignora os dias com valor 0.0 e extrai os dados
        faturamentos = [dia['valor'] for dia in dados if 'valor' in dia and dia['valor'] > 0]
        return faturamentos
    
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. Verifique o formato do arquivo.")
        return []
    
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []
    
#retorna erros inesperados caso o formato esteja inadequado para o código

def main():
#função principal para o resultado

#para ser mais flexível, você deve digitar o nome do arquivo JSON que você baixou no seu computador, no inicio pedimos que se a biblioteca OS não o encontrasse, nos avisasse disso.
    caminho_arquivo = input("Digite o nome do arquivo JSON [EXEMPLO dados.json]: ").strip()
#.strip garante não haja espaços em branco que possam interromper o funcionamento do código
    
    faturamentos = carregar_dados(caminho_arquivo)
    
    if not faturamentos:
        return

    #para calcular o menor valor de faturamento
    menor_valor = min(faturamentos)
    #para calcular o maior valor de faturamento
    maior_valor = max(faturamentos)
    #para calcular a média mensal de faturamento
    media_mensal = sum(faturamentos) / len(faturamentos)
    #conta o número de dias com faturamento acima da média
    dias_acima_media = sum(1 for valor in faturamentos if valor > media_mensal)
    
    #imprime os resultados
    print(f"Menor valor de faturamento: R${menor_valor:.2f}")
    print(f"Maior valor de faturamento: R${maior_valor:.2f}")
    print(f"Número de dias acima da média: {dias_acima_media}")
#esta linha garante que o código abaixo só seja executado se o script for executado diretamente, e não quando importado como um módulo em outro script.
if __name__ == "__main__":
    main()
