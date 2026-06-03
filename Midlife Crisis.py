print("Hello")
height=input("is your height is greater than 120cm?(Y/N)")
if height=="Y":
    age=int(input("Enter your age:"))
    if age<=12:
        bill=5
        photos=input("Want Photos?(Y/N)")
        if photos=="Y":
            bill+=3
            print("Total bill is:",bill)
        else:
            print("Total bill is:", bill)
    if age >= 12 and age <=18:
        bill = 7
        photos = input("Want Photos?(Y/N)")
        if photos == "Y":
            bill += 3
            print("Total bill is:", bill)
        else:
            print("Total bill is:", bill)
    if age >=18:
        if age >= 45 and age <= 55:
            bill = 0
            print("Total bill is:", bill)
        else:
            bill =12
            photos = input("Want Photos?(Y/N)")
            if photos == "Y":
                bill += 3
                print("Total bill is:", bill)
            else:
                 print("Total bill is:", bill)
else:
    print("Not Enough Age,Sorry")
