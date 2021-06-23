'''
Calculando do I.M.C

        O programa deve receber o nome da pessoa que vai ter seu calculo de
        indíce de massa corporal feito, deve também ser solicitado a altura e o peso
        dessa pesso para que seja efetuado o calculo. A regra para o calculo é a seguinte:

        imc = altura / peso * peso

        ao final imprima o imc da pessoa.
'''
#============== DECLARAÇÕES E ATRIBUIÇÕES =====================
flt_inidice_massa_coporal = 0.00
flt_altura_pessoa = 0.00
flt_peso_pessoa = 00.00
str_nome_pessoa = ''

#============== ENTRADAS E ATRIBUIÇÕES ========================
str_nome_pessoa = input('Qual o nome da pessoa que vai calcular o I.M.C : ')
flt_altura_pessoa = float(input('Qual a altura da pessoa : '))
flt_peso_pessoa = float(input('Qual o peso da pessoa  : '))

#============== PROCESSAMENTO E ATRIBUIÇÕES ===================
flt_indice_massa_corporal = flt_altura_pessoa / flt_peso_pessoa ** 2

#============== SAÍDA =====================================
print(f'Peso informado: {flt_peso_pessoa}'.format(flt_peso_pessoa))
print(f'Altura informado: {flt_altura_pessoa}'.format(flt_altura_pessoa))
print(f'O I.M.C {str_nome_pessoa} é {flt_indice_massa_corporal}'.format(str_nome_pessoa, flt_indice_massa_corporal))
