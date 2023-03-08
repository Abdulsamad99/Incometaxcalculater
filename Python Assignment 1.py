slab1 = 2.5
slab2 = 12.5
slab3 = 20
slab4 = 25
slab5 = 32.5
slab6 = 35
name = input("Hi! What is Your Name?\n" )
print("Welcome, " + name) 
working = input("Are you a working professional?  Yes/No\n")
if working == "Yes":
    Company=input("Comapny: ")
    salary =int(input("What is Your Current Salary per month?\n"))
    anualsalary = salary * 12
    if anualsalary <= 600000:
            incometax = 0
    elif anualsalary > 600000 and anualsalary <= 1200000:
            incometax = (anualsalary - 600000)  * slab1 / 100 / 12
    elif anualsalary > 1200000 and anualsalary <= 240000:
            incometax = (anualsalary - 1200000) * (slab2 / 100  / 12) 
    elif anualsalary > 2400000 and anualsalary <= 3600000:
            incometax = (anualsalary - 2400000) * (slab3 / 100  / 12) 
    elif anualsalary > 3600000 and anualsalary <= 6000000:
            incometax = (anualsalary - 3600000) * (slab4 / 100 / 12) 
    elif anualsalary > 6000000 and anualsalary <= 12000000:
            incometax =   (anualsalary - 6000000 )  * (slab5 / 100 / 12) 
    elif anualsalary > 12000000:
            incometax = (anualsalary - 12000000) * (slab6 / 100 / 12) 
    monthlyincome = salary - incometax
    print("Name: ", name ,"\nCompany: ",Company,"\nAnnual Salary:",anualsalary,"\nMonthly Tax: ",incometax,"\nSalary After Tax: ",monthlyincome)       
else:
        print("Thank You For Your Response")
        
