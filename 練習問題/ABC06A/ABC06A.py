a,b = map(int,input().split())
tmp = (a*b)%2
if tmp:
    print("Odd")
else:
    print("Even")