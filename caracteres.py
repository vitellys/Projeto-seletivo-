#função para inverter a string
def inverter_string(s):
#string vazia para armazenar espaço
    resultado = ''
    
    #o programa começa do final da string e vai em direção ao início
    for char in s:
        resultado = char + resultado
    
    return resultado

#função principal para o usúario escrever a string que deseja
def main():
#solicita uma string ao usuário
    string = input("Digite uma string para inverter [EXEMPLO: 'REBECA', '1234']: ")
    
#inverte e imprime o resultado
    string_invertida = inverter_string(string)
    print(f"String invertida: {string_invertida}")

#esta linha garante que o código abaixo só seja executado se o script for executado diretamente, e não quando importado como um módulo em outro script.
if __name__ == "__main__":
    main()
