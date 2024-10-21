num=int(input("Enter the Year: "))
f=num%4
s=num%100
r=num%400
print(f)
print(s)
print(r)
if f==0 and s!=0 or r==0:
    print("Leap year")

else:
    print("--Not a Leap year")