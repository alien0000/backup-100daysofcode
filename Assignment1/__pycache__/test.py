def plusMinus(arr):
    # Write your code here
    posi=0
    negi=0
    zero=0
    for element in arr:
        print(element)
        if element>0:
            posi=posi+1
        elif element<0:
            posi=negi+1
        else:
            zero=zero+1
    a=(posi/len(arr))
    b=(negi/len(arr))
    c=(zero/len(arr))
    print(round(a,6))
    print(round(b,6))
    print(round(c,6))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
