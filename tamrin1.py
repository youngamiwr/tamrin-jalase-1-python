
x = int(input("enter a number 1, 2, 3, 4, 5, 6 or 7 to select wich program to start working: "))
match x:

# زوج یا فرد بودن عدد
    case 1: 
        num = int(input("enter a number to show you if it is odd/even Posetive/Negetive or zero: "))
        if (num == 0):
            print(f"Your number, {num} is even and it is zero")
        elif (num % 2 == 0):
            if (num > 0):
                print(f"Your number, {num} is even and Posetive")
            else:
                print(f"Your number, {num} is even and Negetive")
        else:
            if (num > 0):
                print(f"Your number, {num} is odd and Posetive")
            else:
                print(f"Your number, {num} is odd and Negetive")

# تهیه بیلیط شهر بازی
    case 2:
        age = int(input("enter your age: "))
        if (age < 5 and age > 0):
            print("your ticket is free")
        elif (age >= 5 and age < 18):
            print("you need to pay 50.000 Toman")
        elif (age >= 18 and age < 60):
            print("you need to pay 100.000 Toman")
        elif (age >= 18 and age < 60):
            print("you need to pay 100.000 Toman")
        elif (age > 60):
            print("you need to pay 70.000 Toman")
        else:
            print("you did not enter a valid number")


# تمرین سال کبیسه
    case 3:
        year = int(input("enter a year to see if it is a leap year or a normal year: "))
        if (year % 4 == 0 and year % 100 != 0):
            print(f"{year} is a leap year")
        elif (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
            print(f"{year} is a leap year")
        else:
            print(f"{year} it is a normal year not a leap one")

# تمرین کسر حقوق با مالیات
    case 4:
        salary = float(input("\nPlease enter your salary: "))
        child = input("\ndo you have any children? (y/n)")
        if (salary <= 10_000_000):
            tax = 0
        elif (salary > 10_000_000 and salary <= 25_000_000):
            tax = (salary - 10_000_000) * 0.10
        else:
            tax = ((25_000_000 * 0.10) + ((salary - 25_000_000) * 0.20))
        if (child == 'y'):
            tax -= 500_000

        print(f"""\nyou should pay {tax} tax
and your salary after paying tax is: """ , salary - tax)



# تمرین نمره    
    case 5:
        score = float(input("Enter your Score number: "))
        if (score <= 20):
            if (score >= 17):
                print(f"A - your score {score}- your great.")
            elif (score >= 15):
                print(f"B - your score {score}- your good.")
            elif (score >= 10):
                print(f"C - your score {score}- not bad.")
            else:
                print(f"your score {score}- kharab kardi pesar jan.")
        else:
            print("the entry is out of range")


# تمرین ازمونه رانندگی
    case 6:
        age = int(input("Enter your age: "))
        li = input("do you have lisence (y/n): ") == 'y'
        isdrunk = input("Are you drunk (y/n): ") == 'y'
        
        if (age >= 18 and li and not isdrunk):
            print("you can drive")
        else:
            print("you can't drive")
            
# تمرین تخفیف خرید طلا

    case 7:
        amount = float(input("How much did you buy ? "))
        tier = input("enter your tier (gold / silver / bronze)").lower()
        
        if (amount < 10_000_000):
            if (tier == 'gold'):
                amount *= 0.85
                print(f"you have 15% off and you should pay {amount}")
            elif (tier == 'silver'):
                amount *= 0.90
                print(f"you have 10% off and you should pay {amount}")
            elif (tier == 'bronze'):
                amount *= 0.95
                print(f"you have 5% off and you should pay {amount}")
        else:
            if (tier == 'gold'):
                amount *= 0.80
                print(f"you have 20% off and you should pay {amount}")
            elif (tier == 'silver'):
                amount *= 0.85
                print(f"you have 15% off and you should pay {amount}")
            elif (tier == 'bronze'):
                amount *= 0.90
                print(f"you have 10% off and you should pay {amount}")