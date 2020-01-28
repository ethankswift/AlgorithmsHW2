import math
import sys
import time
import random


def getInput():
    try:
        infile = open('data.txt', 'r')
    except IOError:
        print("File IO Error")
        quit()
    finally:
        return infile.read()

def makeArr(n):
    arr = [random.randrange(0, 10000) for i in range(n)]
    arr.insert(0,n)
    return arr

def putOutput(arr):
    try:
        outfile = open('bad.out', 'w')
    except IOError:
        print("File IO Error")
        quit()
    finally:
        for k in arr:
            outfile.write("%s " % k)
        return

def badSort(arr, alpha, i, j):
    if(arr[j] < arr[i]):
        arr[i], arr[j] = arr[j], arr[i]
    if(j - i > 1):
        m = int(alpha * (j - i + 1))
        badSort(arr, alpha, i, j-m)
        badSort(arr, alpha, i+m, j)
        badSort(arr, alpha, i, j-m)
    return

def main():
    sys.setrecursionlimit(50000)

    for i in range(1, 8):
        start = time.time()
        badSort(makeArr(i*5000), 0.666, 0, i*5000-1)
        print(".66N: ", i*5000, "  Runtime: %s seconds" % (time.time() - start) )

    for i in range(1, 8):
        start = time.time()
        badSort(makeArr(i*5000), 0.75, 0, i*5000-1)
        print(".75N: ", i*5000, "  Runtime: %s seconds" % (time.time() - start) )

    return 0

main()
