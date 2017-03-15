#---------------------------------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#Prof. Jucimar Jr.
#Adham Lucas da Silva Oliveira           1715310001
#Enrique Leão Barbosa Izel               1715310048
#Erik Atilio Silva Rey                   1715310059
#Ulisses Antonio Antonino da Costa       1515090555
#Guilherme Silva de Oliveira             1715310034
#
#Desenhar um polígono com 3 lados iguais. Cada lado uma cor diferente.
#---------------------------------------------------------------------
import turtle  
t = turtle.Pen()
colors = ['green', 'red', 'blue']
for x in range(3):
    t.pencolor(colors[x])
    t.forward(200) 
    t.left(120) 
