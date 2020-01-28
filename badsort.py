import math
import sys

def getInput():
    try:
        infile = open('data.txt', 'r')
    except IOError:
        print("File IO Error")
        quit()
    finally:
        return infile.read()

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
    str = getInput().rstrip().split(" ")
    n = int(str.pop(0))
    arr = list(map(int,str))

    badSort(arr, float(sys.argv[1]), 0, n-1)

    putOutput(arr)
    return 0

main()
