n=int(input("N: "))
print("Dãy số nguyên tố: ", end = "")
for snt in range(1,n+1): #snt tu 1 den n
    p=0 #product
    for i in range(1,snt+1):
        if snt%i==0: 
            p=p+1
    if p==2: #kiem tra snt
        if n%2==0: #chia 2 TH de khong co dau phay o so cuoi
            if snt<(n-1):
                print(snt, end=", ")
            else: # so nguyen to cuoi khong co dau phay
                print(snt)
        else:
            if snt<(n):
                print(snt, end=", ")
            else: # so nguyen to cuoi khong co dau phay
                print(snt) 
