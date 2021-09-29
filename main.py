'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import random 
randomlist = []
d = 500000

ordenada = sorted (randomlist)
'''
    1. Eh importado o modulo random;
    /
    2. Sao criadas as variaveis d com valor ja definido, vetor -> randomlist com 
    espaco a ser preenchido pelo laco de repeticao e ordenada agregando o metodo 
    sorted para ordenar os valores recebidos por parametro de randomlist;
    /
    3. O laco de repeticao ira trazer os valores de forma randomica entre 0 e 500000
    para serem armazenados em randomlist pela funcao append;
    /
    4. Em seguida a variavel ordenada eh exibida com os valores recebidos por 
    paramentro de forma ordenada de menor para maior.
'''
for i in range(d):
    randomlist.append(random.randint(0,d))
    print(ordenada)



