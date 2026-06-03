print("Welcome")
size=input("Enter your pizza size ('S' for small,'M' for medium & 'L' for large) : ")
pepp=input("Add Pepperoni?(Y/N)")
cheese=input("Add extra cheese?(Y/N)")
bill=0
if size=="S":
    bill=15
    if pepp=="Y":
        bill=bill+2
        if cheese=="Y":
            bill=bill + 1
            print("Total Bill : $",bill)
        else:
            print("Total Bill : $",bill)
    else:
        if cheese == "Y":
            bill = bill + 1
            print("Total Bill : $",bill)
        else:
            print("Total Bill : $",bill)

if size=="M":
    bill=20
    if pepp=="Y":
        bill=bill+2
        if cheese=="Y":
            bill=bill + 1
            print("Total Bill : $",bill)
        else:
            print("Total Bill : $",bill)
    else:
        if cheese == "Y":
            bill = bill + 1
            print("Total Bill : $",bill)
        else:
            print("Total Bill : $",bill)

if size=="L":
    bill=25
    if pepp=="Y":
        bill=bill+2
        if cheese=="Y":
            bill=bill + 1
            print("Total Bill : $",bill)
        else:
            print("Total Bill : $",bill)
    else:
        if cheese == "Y":
            bill = bill + 1
            print("Total Bill : $",bill)
        else:
            print("Total Bill : $",bill)
