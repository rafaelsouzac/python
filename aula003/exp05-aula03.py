'''
Supondo que a população do país Cascãolandia seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de Cebolinhovisk seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população de Cascãolandia ultrapasse ou iguale a população
do Cebolinhovisk, mantidas as taxas de crescimento.
'''

#======== DECLARAÇÕES E ATRIBUIÇÕES INICIAIS ===============
flt_populacao_cascaolandia = 80000.0
flt_taxa_crescimento_cascaolandia = 3.0
flt_populacao_cebolinhovisk = 200000.0
flt_taxa_crescimento_cebolinhovisk = 1.5

int_numero_anos_iguala_populacao = 1

#======== PROCESSAMENTO ===============================

while not flt_populacao_cascaolandia >= flt_populacao_cebolinhovisk:
    flt_populacao_cascaolandia = ((flt_populacao_cascaolandia/100)*flt_taxa_crescimento_cascaolandia) + flt_populacao_cascaolandia
    flt_populacao_cebolinhovisk = ((flt_populacao_cebolinhovisk/100)*flt_taxa_crescimento_cebolinhovisk) + flt_populacao_cebolinhovisk
    int_numero_anos_iguala_populacao = int_numero_anos_iguala_populacao + 1
else:
    print(f'Levará {int_numero_anos_iguala_populacao} anos para a população de Cascolandia igualar ou ser maior que a de Cebolinhovisk'.format(int_numero_anos_iguala_populacao))
    print(f'População de Cebolinhovisk = {flt_populacao_cebolinhovisk}  População de Cascãolandia = {flt_populacao_cascaolandia}'.format(flt_populacao_cebolinhovisk, flt_populacao_cascaolandia))