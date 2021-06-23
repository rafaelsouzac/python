#Faça um Programa que peça dois números e imprima a soma.

#============== DECLARAÇÕES E ATRIBUIÇÕES =====================
primeiro_numero = 0
segundo_numero = 0
soma_dos_numeros = 0
#============== ENTRADAS E ATRIBUIÇÕES ========================
primeiro_numero = float(input('Insira o valor do primeiro número: '))
segundo_numero = float(input('Insira o valor do segundo número: '))

#============== PROCESSAMENTO E ATRIBUIÇÕES ===================
soma_dos_numeros = primeiro_numero + segundo_numero

#============== SAÍDA =========================================
print(f'O valor da soma dos dois números é {soma_dos_numeros}'.format(soma_dos_numeros))