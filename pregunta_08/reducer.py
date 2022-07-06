#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    curkey = None
    total = 0
    for line in sys.stdin:
        letra, fecha, numero = line.split("\t")
        numero = int(numero)
        if letra == curkey:
            total += numero
            c += 1
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, float(total),total/c))
            curkey = letra
            total = numero
            c= 1

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, float(total),total/c))