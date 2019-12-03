
A = int(input()) # 500
B = int(input()) # 100
C = int(input()) # 50
X = int(input())
count = 0
"""
a_max = int(X/500)
if a_max > A:
    a_max = A

for a in range(a_max+1):
    X_a = X - 500*a

    b_max = int(X_a/100)

    if b_max > B:
        b_max = B

    for b in range(b_max+1):
        X_b = X_a - 100*b
        c = int(X_b/50)

        if c > C:
             continue

        X_c = X_b - 50*c
        if X_c == 0:
            count+=1
"""
            
#全探索
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            total = 500*a + 100*b + 50*c
            if(total==X):
                count+=1
print(count)




