def multiplication_table(m, n):
    for row in range(1,10):
        for col in range(m,n+1):
            print("{1}x{0}={2}\t".format(row , col , row*col),end='')
        print();

def pyramid(n):
    rows = int(n)
    s = '*'
    for i in range(1, rows):
        print((s * (2*i-1)).center(2*rows-1))
    print();
