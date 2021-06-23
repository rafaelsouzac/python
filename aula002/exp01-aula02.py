#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

#============== DECLARAÇÕES E ATRIBUIÇÕES =====================
flt_valor_solicitado = 0.00
str_valor_positivo_ou_negativo= ''
str_entrada = ''
#============== ENTRADAS E ATRIBUIÇÕES ========================
str_entrada = input('Digite um valor qualquer. Deve ser Número: ')

#============== PROCESSAMENTO E ATRIBUIÇÕES ===================

if str_entrada.isnumeric():

    flt_valor_solicitado = float(str_entrada)

    if flt_valor_solicitado > 0:
        str_valor_positivo_ou_negativo = 'Valor Informado é positivo.'
    elif flt_valor_solicitado < 0:
        str_valor_positivo_ou_negativo = 'Valor Informado é negativo.'
    else:
        str_valor_positivo_ou_negativo = 'Valor Informado é zero ou não é número.'
else:
    str_valor_positivo_ou_negativo = 'Você digitou um dado inválido.'
#============== SAÍDA =========================================
print(str_valor_positivo_ou_negativo)