#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        renglon = line.split(',')
        letra =  renglon[0]
        numero = renglon[1].replace("\n", "")
        sys.stdout.write("{}\t{}\n".format(numero,letra))