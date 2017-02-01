def investmentVal(amount, annualRate, years):
    monthlyInterestRate = annualRate/12.0/100
    months = years*12.0
    futureInvestmentValue = round(amount*((1+monthlyInterestRate)**months),2)
    return futureInvestmentValue