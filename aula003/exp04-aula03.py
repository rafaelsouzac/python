# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

#============== DECLARAÇÕES E ATRIBUIÇÕES =====================
int_numero_fator = 0
int_valor_decrementado = 0
int_valor_acumulado = 0
str_valor_digitado = ''
bol_valor_correto = False
str_saida = ''
#============== ENTRADAS E ATRIBUIÇÕES ========================
while not bol_valor_correto:
    str_valor_digitado = input('Digite o numero do fatorial: ')
    if str_valor_digitado.isdigit():
        int_numero_fator = int(str_valor_digitado)
        str_saida = str_valor_digitado + '!='
        int_valor_decrementado = int_numero_fator
        while int_valor_decrementado > 1:
            if int_valor_decrementado == int_numero_fator:
                int_valor_acumulado = int_valor_decrementado * int_numero_fator
            else:
                int_valor_acumulado *= int_valor_decrementado
            int_valor_decrementado = int_valor_decrementado - 1
    else:
        pass
#============== PROCESSAMENTO E ATRIBUIÇÕES ===================

#============== SAÍDA =========================================
