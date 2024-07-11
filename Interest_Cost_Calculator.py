# Interest Cost Calculator

## Input principal rate and years of payment
def simple_interest(principal,years,rate):
    float(input('Enter the principal amount: ', principal))
    float(input('Enter the year of return: ', years))
    float(input('Enter the rate of payment: ', rate))
     
    interestCost = (principal * years * rate)/100
     
    print(f'Interest Cost in USD is:', interestCost)
    return interestCost
