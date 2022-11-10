
print("Welcome to the Prince Health Management System\n")
lock = 1
retrieve = 2
diet = 1
exercise = 2
Harry = 1
Rohan = 2
Pooja = 3


def getdate():
    import datetime
    return datetime.datetime.now()


time = str(getdate())

a = int(input("enter your choice\n" + "1 for lock and 2 for retrieve\n"))
b = int(input("choose diet by pressing 1 and exercise by pressing 2\n"))
c = int(input("enter the name\n" + "1 for Harry, 2 for Rohan and 3 for Pooja\n"))

if a == lock and b == diet and c == Harry:
    with open("Harry Diet", "a") as f1:
        f1.write(" \n")
        f1.write(time + "   - ")
        print(f1.write(input("\nwrite what you want to add in your diet\n")))

if a == lock and b == diet and c == Rohan:
    with open("Rohan Diet.txt", "a") as f2:
        f2.write(" \n")
        f2.write(time + "   - ")
        print(f2.write(input("\nwrite what you want to add in your diet\n")))

if a == lock and b == diet and c == Pooja:
    with open("Pooja Diet.txt", "a") as f3:
        f3.write(" \n")
        f3.write(time + "   - ")
        print(f3.write(input("\nwrite what you want to add in your diet\n")))

if a == lock and b == exercise and c == Harry:
    with open("Harry Exercise", "a") as f1:
        f1.write(" \n")
        f1.write(time + "   - ")
        print(f1.write(input("\nwrite what you want to add in your exercise\n")))

if a == lock and b == exercise and c == Rohan:
    with open("Rohan Exercise.txt", "a") as f2:
        f2.write(" \n")
        f2.write(time + "   - ")
        print(f2.write(input("\nwrite what you want to add in your exercise\n")))

if a == lock and b == exercise and c == Pooja:
    with open("Pooja Exercise.txt", "a") as f3:
        f3.write(" \n")
        f3.write(time + "   - ")
        print(f3.write(input("\nwrite what you want to add in your exercise\n")))

if a == retrieve and b == exercise and c == Harry:
    with open("Harry Exercise", "rt") as f4:
        print(f4.read())

if a == retrieve and b == exercise and c == Rohan:
    with open("Rohan Exercise.txt", "rt") as f5:
        print(f5.read())

if a == retrieve and b == exercise and c == Pooja:
    with open("Pooja Exercise.txt", "rt") as f6:
        print(f6.read())

if a == retrieve and b == diet and c == Harry:
    with open("Harry Diet", "rt") as f4:
        print(f4.read())

if a == retrieve and b == diet and c == Rohan:
    with open("Rohan Diet.txt", "rt") as f5:
        print(f5.read())

if a == retrieve and b == diet and c == Pooja:
    with open("Pooja Diet.txt", "rt") as f6:
        print(f6.read())
