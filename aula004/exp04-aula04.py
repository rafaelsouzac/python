#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
#Imprima os três vetores.

lst_int_numero_digitados = []
lst_int_pares = []
lst_int_impares = []
bol_programa_rodando = True
int_controle = 20
int_contador = 0
while int_contador < int_controle:
    str_entrada_usuario = input('Digite um número positivo qualquer: ')
    if str_entrada_usuario.isdigit():
        lst_int_numero_digitados.append(int(str_entrada_usuario))
        if(lst_int_numero_digitados[int_contador] % 2 == 0):
            lst_int_pares.append(lst_int_numero_digitados[int_contador])
        else:
            lst_int_impares.append(lst_int_numero_digitados[int_contador])
        int_contador += 1
    else:
        print('Valor digitado errado. Tente Novamente')
        print('======================================')

print('Número Digitados: '+str(lst_int_numero_digitados))
print('==================================================')
print('Número Pares Digitados: '+str(lst_int_pares))
print('==================================================')
print('Número Impares Digitados: '+str(lst_int_impares))
print('==================================================')