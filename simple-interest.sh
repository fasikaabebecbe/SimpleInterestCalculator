# Interest Cost Calculator

## Input principal rate and years of payment
principal =float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of payment: "))
years = float(input("Enter the year of return: "))

## Calculate Interest
interest_cost = principal * years * rate / 100

## Display the result of interest
print(f"Interest Cost: {interest_cost} USD")
