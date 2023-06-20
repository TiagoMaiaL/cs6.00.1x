# The solution to the second exercise of the problem set 2:
#
# Now write a program that calculates the minimum fixed monthly payment needed 
# in order pay off a credit card balance within 12 months. By a fixed monthly 
# payment, we mean a single number which does not change each month, 
# but instead is a constant amount that will be paid each month.

balance = 3329
annual_interest_rate = 0.2

def find_ideal_monthly_payment(balance, annual_interest_rate):
  guess = 10
  while True:
    remaining_balance = compute_year_remaining_balance(balance, annual_interest_rate, guess)
    if remaining_balance > 0:
      guess += 10
    else:
      break
  return guess

def compute_year_remaining_balance(initial_balance, annual_interest_rate, monthly_payment):
  balance = initial_balance
  monthly_interest_rate = annual_interest_rate / 12.0
  for month in range(0, 12):
    balance -= monthly_payment
    balance += balance * monthly_interest_rate
  return balance
  
ideal_monthly_payment = find_ideal_monthly_payment(balance, annual_interest_rate)
print("Lowest Payment: " + str(ideal_monthly_payment))
