def verificar(numero):
    if numero < 0:
     return False  #Se o número for negativo, não pertence  sequência 

    #Estabelecer a base para iniciar a sequência
    anterior, atual = 0, 1

    #Cria um loop que continua calculando enquanto atual for maior que n
    while atual < numero:
        #Atualiza os números da sequência
        anterior, atual = atual, anterior + atual

    #Verifica se o número pertence a sequência 
    return numero == atual or numero == 0

#Pede ao usuário para digitar o número que ele deseja verificar se pertence à sequência 
verificar_o_numero = int(input("Digite o número que deseja para verificar se pertence à sequência fibonacci: "))

#Chama a função para imprimir o resultado
if verificar(verificar_o_numero):
    print(f"O número {verificar_o_numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {verificar_o_numero} NÃO pertence à sequência de Fibonacci.")
