# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

#============== DECLARAÇÕES E ATRIBUIÇÕES =====================
str_dia_semana = ''
int_numero_digitado = 0

#============== ENTRADAS E ATRIBUIÇÕES ========================
int_numero_digitado = int(input('Digite um número entre 1 a 7'))

#============== PROCESSAMENTO E ATRIBUIÇÕES ===================
if int_numero_digitado == 1
    str_dia_semana = 'Dia da Semana é Domingo'
elif int_numero_digitado == 2:
    str_dia_semana = 'Dia da Semana é Segunda-Feria'
elif int_numero_digitado == 3:
    str_dia_semana = 'Dia da Semana é Terça-Ferira'
elif int_numero_digitado == 4:
    str_dia_semana = 'Dia da Semana é Quarta-Feira'
elif int_numero_digitado == 5:
    str_dia_semana = 'Dia da Semana é Quinta-Feira'
elif int_numero_digitado == 6:
    str_dia_semana = 'Dia da Semana Sexta-Feira'
elif int_numero_digitado == 6:
    str_dia_semana = 'Dia da Semana Sábado'
else:
    str_dia_semana = 'Valor digitado inválido'
#============== SAÍDA =========================================
print(str_dia_semana)