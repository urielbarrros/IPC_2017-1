#-----------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#Prof. Jucimar Jr.
#Gabriel Barroso da Silva Lima     -|- 1715310011
#Wesley da Silva Rocha             -|- 1715310026
#Rodolfo gomes do nascimento       -|- 1515200550
#Victor Hugo de Oliveira Carreira  -|- 1715310063
#Diego Reis Figueira               -|- 1515070169
#Faça um Programa para uma loja de tintas. O programa deverá pedir o
# tamanho em metros quadrados da área a ser pintada. Considere que a
# cobertura da tinta é de 1 litro para cada 6 metros quadrados e que
# a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   comprar apenas latas de 18 litros;
#   comprar apenas galões de 3,6 litros;
#   misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de
#    folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

mq = float(input("tamanho em metros quadrados da área a ser pintada: "))
t = mq/6
l = int(t/18) #l recebe o valor aproximado de t/18
g = int(t/3.6) #g recebe o valor aproximado de t/3,6
if l < (t/18): #se l for menor que t/18, significa que precisará de mais tinta, sendo necessária mais uma lata
    print("Você precisará de ", t," litros de tinta, ", l+1," latas e pagará R$ ", (l+1)*80)
else: #se l for maior que t/18, significa que já tem latas suficientes
    print("Você precisará de ", t," litros de tinta, ", g," latas e pagará R$ ", l*80)
if g < (t/3.6): #se g for menor que t/3,6, significa que precisará de mais tinta, sendo necessária mais um galão
    print("Você precisará de ", t," litros de tinta, ", g+1," latas e pagará R$ ", (g+1)*25)
else: #se g for maior que t/3.6, significa que já tem latas suficientes
    print("Você precisará de ", t," litros de tinta, ", g," latas e pagará R$ ", g*25)
t *= 1.1 #colocado o acréscimo de 10 por cento
l *= 1.1 #colocado o acréscimo de 10 por cento
e = (t%18)/3.6 #calculado a previsão de galãos
print("Você precisa de ", t," litros de tinta, ", l," latas, ", e," galões e custará R$ ", (l*80)+(e*25)) #feito os cálculos para os dados necessários