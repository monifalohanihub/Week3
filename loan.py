age = int(input("Enter your age:"))
income = float(input("Enter your monthly income: "))
job = input("Do you have a valid job? ")
loan = float(input("How much loan do you want to apply for? "))  
while True:     
 if age >= 21: 
    if job.lower() == "yes":
        if income >= 30000:
            if loan <= 1000000:
                print("You are eligible for a loan.")
            else:
                print("You are not eligible for a loan because the requested amount exceeds the maximum limit of 1000000.")
        else:
            print("You are not eligible for a loan because your income is less than 30000.")
    else:
        print("You are not eligible for a loan because you do not have a valid job.")
else:
    print("You are not eligible for a loan because you are under 21 years old.")
if income >= 30000 and income < 49999:
    max_loan = 300000
    print("You are eligible for a loan of 300000.") 
elif income >= 50000 and income < 79999:
    max_loan = 500000
    print("You are eligible for a loan of 500000.")
elif income >= 80000 and income < 99999:
    max_loan = 800000   
    print("You are eligible for a loan of 800000.")   
elif income >= 100000:
    max_loan = 1000000
    print("You are eligible for a loan of 1000000.")
else:
    print("You are not eligible for a loan because your income is less than 30000.") 
print("you can apply for a loan of", max_loan) 
print("you have requested a loan of", loan)
print("your loan has been approved for the amount of", loan)      
