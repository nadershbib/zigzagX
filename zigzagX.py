def X(number):
    d = number
    a = 1
    b = d
    for h in range(d):
        for g in range(1, d + 1):
            if g == a:
                print("▓", end="")

            if g == b:
                print("▓", end="")
            print(" ", end="")
        a += 1
        b -= 1
        print()


def zigzag(num):
    l = 1
    for x in range(num):
        for y in range(l):
            print(" ", end="")
        print("▓")
        l += 3

    for r in range(num):
        for u in range(l):
            print(" ", end="")
        print("▓")
        l -= 3
    print(" ▓")





def iterateAll(numm):
    count = 1
    i = q = 1
    while count <= numm:
        while i <= 70:
            zigzag(i)
            i += 1
        while i >= 1:
            zigzag(i)
            i -= 1
        while q <= 150:
            X(q)
            q += 1
        while q >= 1:
            X(q)
            q -= 1
        count+=1
def iterateX(n):
    i=1
    d=1
    while i<=n:
        while d<=150:
            X(d)
            d+=1
        while d>=1:
            X(d)
            d-=1
        i+=1


iterateAll(3)
iterateX(5)