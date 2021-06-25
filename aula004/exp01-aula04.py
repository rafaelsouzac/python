'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela conforme o exemplo abaixo:
+----------+------------
+ Notas    +  Valor    +
+-----------------------
+   1º     +  7.5      +
+-----------------------
+   2º     +  8.0      +
+-----------------------
+   3º     +  7.0      +
+-----------------------
+   4º     +  5.0      +
+-----------------------
+   Média  +  23.75    +
+-----------------------
Para isso utilize lista, dicionario ou tupla
'''

bol_notas_inseridas = False
lst_flt_notas = []
str_valor_digitado_usuario = ''
int_numero_nota = 1
flt_media = 0.00
while not bol_notas_inseridas:
    str_texto_para_usuario = 'Digite a '+str(int_numero_nota)+'º nota: '
    str_valor_digitado_usuario = input(str_texto_para_usuario)
    if str_valor_digitado_usuario.isdigit():
        lst_flt_notas.append(float(str_valor_digitado_usuario))
        
        if int_numero_nota == 4:
            bol_notas_inseridas = True
        int_numero_nota = int_numero_nota + 1
    else:
        print('Valor Invalido, digite novamente')
        print('================================================')
    
flt_media = sum(lst_flt_notas) / 4
print(f'A media dos valores inserido é {flt_media}'.format(flt_media))