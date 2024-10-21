num=int(input("Enter the Marks: "))
if num>=90 and num<=100:
    print("A")
elif num>=80 and num<=89:
    print("B")
elif num >=70 and num <=79:
    print("C")
elif num >=60 and num <=69:
    print("D")
elif num >= 0 and num <= 59:
    print("Fail")
else:
    print("Invalid score")