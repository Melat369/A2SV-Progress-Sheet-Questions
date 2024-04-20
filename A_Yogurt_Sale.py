t = int(input())

for _ in range(t):
    n,a,b = map(int,input().split())
    res = []
    price = 0



    if n%2==0:
        if (n*a) > (n*b/2):
            price += b*n/2
            res.append(price)
        else:
            price += n*a
            res.append(price)
    if n%2 != 0:
        if ((n-1)*a) > ((n-1)*b/2):
            price +=( a+(n-1)*b/2)
            res.append(price)
        else:
            price += (a+ (n-1)*a)
            res.append(price)
    print (int(*res))
























