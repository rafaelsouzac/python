# Convertendo temperatura Celius para Fahrenheit

#============== DECLARAÇÕES E ATRIBUIÇÕES =====================
temperatura_celcius = 00.0
temperatura_fahrenheit = 000.00

#============== ENTRADAS E ATRIBUIÇÕES ========================
temperatura_celcius = float(input('Digite a temperatura em Celcius: '))

#============== PROCESSAMENTO E ATRIBUIÇÕES ===================
temperatura_fahrenheit = temperatura_celcius * 1.8 + 32

#============== SAÍDA =====================================
print(f'A temperatura informada em Celcius foi: {temperatura_celcius} , convertira para Fahrenheit fica: {temperatura_fahrenheit}'.format(temperatura_celcius,
                                                                                                                                          temperatura_fahrenheit)