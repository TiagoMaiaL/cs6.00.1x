# The solution to the second exercise of the problem set 2:
#
# Use bisection search to find the minimum monthly payment necessary to
# pay off a credit card balance within 12 months.

balance = 320000
annual_interest_rate = 0.2

def find_ideal_monthly_payment(balance, annual_interest_rate):
  monthly_interest_rate = annual_interest_rate / 12
  lower = balance / 12.0
  upper = (balance * ((1 + monthly_interest_rate) ** 12)) / 12.0
  epsilon = -0.01
  guess = ((upper - lower) / 2) + lower
  while True:
    remaining_balance = compute_year_remaining_balance(balance, annual_interest_rate, guess)
    if remaining_balance < 0 and remaining_balance >= epsilon:
      break
    else:
      if remaining_balance > 0:
        lower = guess
      else:
        upper = guess
      guess = ((upper - lower) / 2) + lower
  return guess

def compute_year_remaining_balance(initial_balance, annual_interest_rate, monthly_payment):
  balance = initial_balance
  monthly_interest_rate = annual_interest_rate / 12.0
  for month in range(0, 12):
    balance -= monthly_payment
    balance += balance * monthly_interest_rate
  return balance
  
ideal_monthly_payment = find_ideal_monthly_payment(balance, annual_interest_rate)
print("Lowest Payment: " + str(round(ideal_monthly_payment, 2)))
