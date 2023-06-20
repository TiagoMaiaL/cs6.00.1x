# Solution to the first exercise in the problem set 2:
#
# Write a program to calculate the credit card balance after one year if 
# a person only pays the minimum monthly payment required by the credit 
# card company each month.

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12.0

for month in range(1, 13):
  minimumMonthlyPayment = balance * monthlyPaymentRate
  balance -= minimumMonthlyPayment
  balance += balance * monthlyInterestRate
  print("Month " + str(month) + " Remaining balance: " + str(round(balance, 2)))

print("Remaining balance " + str(round(balance, 2)))
