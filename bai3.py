a = int(input("Enter your number: "))
p=0 #product 

for i in range(1,a+1):
    if a%i==0:
        p=p+1

if p==2: # snt chỉ chia hết cho 2 số là: 1 và chính nó
    print("Day la so nguyen to")
else:
    print("Day khong phai la so nguyen to")