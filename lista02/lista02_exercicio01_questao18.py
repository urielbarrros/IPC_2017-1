#-----------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#Prof. Jucimar Jr.
#Gabriel Barroso da Silva Lima     -|- 1715310011
#Wesley da Silva Rocha             -|- 1715310026
#Rodolfo gomes do nascimento       -|- 1515200550
#Victor Hugo de Oliveira Carreira  -|- 1715310063
#Diego Reis Figueira               -|- 1515070169
#Faça um programa que peça o tamanho de um arquivo
# para download (em MB) e a velocidade de um link
# de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link
# (em minutos).

a = float(input("tamanho do arquivo (em MB): "))
i = float(input("velocidade da internet (em Mbps): "))
print("tempo aproximado de download (em minutos): ", a/(i*7.5)) #Tamanho do arquivo é dividido pela velocidade convertida em MBpm (internet multiplicado por 60 para passar de segundos para minutos e dividida por 8 para converter de Mb para MB)