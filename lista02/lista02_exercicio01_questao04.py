# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros                      1715310043
# Gabriel Nascimento de Oliveira            1715310052
# Luiz Daniel Raposo Nunes de Mello	        1715310049
# Renan de Almeida Campos                   0825060036
# Tiago Ferreira Aranha 	                1715310047
# Wilbert Luís Evangelista Marins           1715310055
# Mackson Garcez Moreno de Oliveira júnior  1215090300
#
# 1.4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média
# ----------------------------------------------------------

nota_1 = float(input('Informe a sua nota do primeiro bimestre:'))
nota_2 = float(input('Informe a sua nota do segundo bimestre:'))
nota_3 = float(input('Informe a sua nota do terceiro bimestre:'))
nota_4 = float(input('Informe a sua nota do quarto bimestre:'))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print('Média dos quatro bimestres: %2.1f' % media)