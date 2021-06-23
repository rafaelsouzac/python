'''
#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem
    ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
'''
#============== DECLARAÇÕES E ATRIBUIÇÕES =====================
flt_lado1 = 0.00
flt_lado2 = 0.00
flt_lado3 = 0.00

flt_soma_lado1_lado2 = 0.00 # tem que ser > lado3
flt_soma_lado1_lado3 = 0.00 # tem que ser > lado2
flt_soma_lado2_lado3 = 0.00 # tem que ser > lado1

str_tipo_de_triangulo = ''
#============== ENTRADAS E ATRIBUIÇÕES ========================
flt_lado1 = float(input('Digite o primeiro lado do triangulo: '))
flt_lado2 = float(input('Digite o segundo  lado do triangulo: '))
flt_lado3 = float(input('Digite o terceiro lado do triangulo: '))

#============== PROCESSAMENTO E ATRIBUIÇÕES ===================
flt_soma_lado1_lado2 = flt_lado1 + flt_lado2
flt_soma_lado1_lado3 = flt_lado1 + flt_lado3
flt_soma_lado1_lado2 = flt_lado2 + flt_lado3

if (flt_soma_lado1_lado2 > flt_lado3) or (flt_soma_lado1_lado3 > flt_lado2) or (flt_soma_lado2_lado3 > flt_lado1):
    if(flt_lado1 == flt_lado2 and flt_lado1 == flt_lado3):
        str_tipo_de_triangulo = 'Triângulo do tipo equilátero'
    elif(flt_lado1 == flt_lado2) or (flt_lado1 == flt_lado3) or (flt_lado2 == flt_lado3):
        str_tipo_de_triangulo = 'Triângulodo tipo isóceles'
    else:
        str_tipo_de_triangulo = 'Triângulodo tipo escaleno'
else:
    str_tipo_de_triangulo = 'Os dados informando não formam um triangulo.'

#============== SAÍDA =========================================
print(str_tipo_de_triangulo)