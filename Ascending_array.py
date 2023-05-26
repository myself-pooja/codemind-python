n=int(input())
arr=list(map(int,input().split()))
if(arr==sorted(arr)):
    c=0
    for i in arr:
        if arr.count(i)>1:
            c=1
            print('no')
            break
        if c==1:
            break
    if c==0:
        print('yes')
else:
    print('no')