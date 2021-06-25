#Faça um Programa que leia um vetor de 5 números inteiros e positivo e mostre-os.

bol_executa_programa = True
lst_int_numeros = []
str_entrada_usuario = ''
int_controler = 5
int_volta     = 1

while int_controler >= int_volta:
    str_entrada_usuario = input('Digite um valor inteiro e positivo: ')
    if str_entrada_usuario.isdigit() and int(str_entrada_usuario) > -1:
        lst_int_numeros.append(int(str_entrada_usuario))
        int_volta += 1
    else:
        print('Valor digitado esta incorreto, digite novamente.')
        print('================================================')


print(lst_int_numeros)
