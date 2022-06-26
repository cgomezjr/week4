print("Chart of teacher's salary based on years of experience")
startSalary = int(input("Enter the starting salary: "))
percIncrease = int(input("Enter the percentage increase: "))
numYears = int(input("Enter the number of years in the schedule: ")) - 1

percIncrease = percIncrease / 100
year = 0

while numYears < 0 or numYears > 9:
        numYears = int(input("Enter a number between 1 and 10: ")) - 1

while numYears >= 0:
        newSalary = "{:.2f}".format(startSalary)
        startSalary = round(startSalary * (percIncrease + 1), 2)
        numYears -= 1
        year += 1
        print("%3s" % year, "%10s" % newSalary)

