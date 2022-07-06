#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        renglon = line.split('   ')
        letra =  renglon[0]
        fecha =  renglon[1]
        numero = int(renglon[2])
        sys.stdout.write("{}\t{}\t{}\n".format(letra,fecha, numero))