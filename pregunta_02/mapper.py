#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        amount = line.split(',')
        monto =  amount[4]
        destino = amount[3]
        sys.stdout.write("{}\t{}\n".format(destino,monto))