# printTriangle(n)
# author @Yichen
def printTriangle(n):
    for i in range(n):
        if i+1<(n+1)/2:
            for a in range(i+1):
                print('*',end=" ")
        elif i+1 == (n+1)/2:
            for a in range(i+1):
                print('*',end=" ")
        else:
            for a in range(n-i):
                print('*',end=" ")
        print("")

if __name__ == '__main__':
    printTriangle(9)

