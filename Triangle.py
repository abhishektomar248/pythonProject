from lib2to3.pgen2.tokenize import single3prog

s1=int(input("Enter the side1: "))
s2=int(input("Enter the side2: "))
s3=int(input("Enter the side3: "))

if s1==s2 and s1==s3 and s2==s3:
 print("equilateral")
elif s1!=s2 or s1!=s3:
     print("Isoceles")
else:
     print("Scalen")