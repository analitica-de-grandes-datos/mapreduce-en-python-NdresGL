#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from ssl import OP_NO_RENEGOTIATION
import sys
if __name__ == "__main__":
    menor = 1000
    lista=[]
    Newlist=[]
    for line in sys.stdin:
        lista.append(str(line))
    while len(lista)>0:
        menor = 1000
        i = 0
        for line in lista:
            numero, letra = str(line).replace('\n','').split('\t')
            if menor >= int(numero):
                menor = int(numero)
                letramin = letra
                borrar=line
                i = 1
        if i == 1:
            lista.remove(borrar)
            sys.stdout.write("{},{}\n".format(letramin, menor))