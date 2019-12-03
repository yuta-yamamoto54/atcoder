N = int(input())
A = list(map(int,input().split(" ")))
count = 0
flag = False

#自分のコード
#while True:
#    for i in range(N):
#        a = A[i] % 2
#        if a == 1:
#            flag = True
#            break
#        else:
#            A[i] = A[i] / 2
#    if flag:
#        break
#    else:
#        count += 1
  
##総論理和をとって
bit = A[0]
for b in A[1:]:
    #論理和OR
    #奇数が一つでも存在すれば必ず一桁目が1となる
    #二桁目が1の時は2で割った各種の値に奇数が含まれるとき
    bit = bit | b
result = 0

##シフト回数を数える
##一桁目が０であるなら論理積が０となって偶数
while(bit!=0) and ((bit&1)==0):
    result += 1
    #シフトして割る２
    bit = bit>>1

print(result)