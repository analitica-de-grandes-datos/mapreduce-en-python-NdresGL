#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    curkey = None
    mayor=0.0000
    menor=1000.0
    for line in sys.stdin:
        key, val = line.split("\t")
        val = float(val)
        if key == curkey:
            if mayor < val:
                mayor = val
            if menor > val:
                menor=val
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey,mayor,menor))
            curkey = key
            mayor = float(val)
            menor=val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, mayor,menor))