import csv
from pathlib import Path

"""Part 1: Automate the Calculations."""

loan_costs = [500, 600, 200, 1000, 450]

print("Part 1: Automate the Calculations\n")
# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!
total_number_of_loans = len(loan_costs)

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!
print(f"1)The total number of loans are: {total_number_of_loans}")

# What is the total of all loans?
# Use the `sum` function to calculate the total of all loans in the list.
total_value_of_loans = sum(loan_costs)

# Print the total value of the loans - 2 decimal places
print(f"2)The total value of the loans is:$ {total_value_of_loans:,.2f}")

# What is the average loan amount from the list?
# Using the sum of all loans and the total number of loans, calculate the average loan price.
average_loan_amount = total_value_of_loans / total_number_of_loans

# Print the average loan amount - 2 decimal places
print(f"3)The average Loan Amount of loans is:$ {average_loan_amount:,.2f}\n")

"""Part 2: Analyze Loan Data."""

print("Part 2: Analysis of Loan data\n")

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!

loan_price = loan.get("loan_price")
remaining_months = loan.get("remaining_months")
future_value = loan.get("future_value")

print(f"1)Remaining months in the loan are: {remaining_months}")
print(f"2)Future value of the loan is: ${future_value:,.2f}")
print(f"3)Loan price is: ${loan_price:,.2f}")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
# YOUR CODE HERE!
discount_rate = 0.2
present_value = future_value / (1 + (discount_rate/12)) ** remaining_months
print(f"4)The Present value of the loan is :${present_value:,.2f}")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

if present_value >= loan_price:
    print("5)The loan is worth at least the cost to buy it\n")
else:
    print("5)Loan is too expensive and not worth the price\n")

print("Part 3: Financial Calculations\n")   

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!

loan_price = new_loan.get("loan_price")
remaining_months = new_loan.get("remaining_months")
future_value = new_loan.get("future_value")

##print(f"3)Loan price is:  YYY ${loan_price:,.2f}")
##print(f"1)Remaining months in the loan are:YYYY {remaining_months}")
##print(f"2)Future value of the loan is:YYY ${future_value:,.2f}")

def calculate_present_value(future_value,discount_rate,remaining_months):
    present_value = future_value / (1 + (discount_rate/12)) ** remaining_months
    print(f"The present value of the new loan is:  ${present_value:,.2f}")
    return present_value
     
present_value = calculate_present_value(future_value,discount_rate,remaining_months)

print(f"Present value funtion is: ${present_value:,.2f}\n")


print("Part 4: Conditionally filter lists of loans\n")
"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# @TODO: Print the `inexpensive_loans` list


inexpensive_loans=[]
#Created a second list for alternative solution of the question
inexpensive_loans2=[]

for i in loans:
   
      if i["loan_price"] <= 500:

        inexpensive_loans.append(i["loan_price"])
#Created a second list 
        inexpensive_loans2.append(i)       
print("Option 1 for only values for least expensive loans\n")           
print(inexpensive_loans)
print("Option 2 for complete information about least expenive loans\n")
print(inexpensive_loans2)
#print(loans)
        

with open('inexpensive_loans_IG.csv', 'w', encoding='UTF8',newline='') as forexcel:
    fieldnames = ['loan_price', 'remaining_months','repayment_interval','future_value']   
    writer = csv.writer(forexcel)
    writer.writerow(fieldnames)
    #for i in inexpensive_loans2:
        #writer.writerow([inexpensive_loans2])
    writer = csv.DictWriter(forexcel, fieldnames=fieldnames)
    #writer.writeheader()
    writer.writerows(inexpensive_loans2)
    #csv_writer = csv.writer(csv_file, delimiter=",")

    #for inexpensive_loan in inexpensive_loans2:
        #csv_writer.writerow(inexpensive_loan.values())
