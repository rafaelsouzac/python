#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

#============== DECLARAÇÕES E ATRIBUIÇÕES =====================
str_vogal_consoante = ''
int_codigo_asc = 0

#============== ENTRADAS E ATRIBUIÇÕES ========================
str_vogal_consoante = input('Digite uma letra: ')

#============== PROCESSAMENTO E ATRIBUIÇÕES ===================
if len(str_vogal_consoante) > 1:
    str_vogal_consoante = 'Você digitou mais de uma letra.'
elif str_vogal_consoante[0].isnumeric():
    str_vogal_consoante = 'Você deveria ter digitado uma letra.'
else:
    int_codigo_asc = ord(str_vogal_consoante.title())
    if (int_codigo_asc > 64 and int_codigo_asc < 91):
        if (int_codigo_asc == 65 or int_codigo_asc == 69 or int_codigo_asc == 73 or int_codigo_asc == 79 or int_codigo_asc == 85):
            str_vogal_consoante = 'Você digitou uma vogal.'
        else:
            str_vogal_consoante = 'Você digitou uma consoante.'
    else:
        str_vogal_consoante = 'Você não digitou uma letra'

#============== SAÍDA =========================================
print(str_vogal_consoante)