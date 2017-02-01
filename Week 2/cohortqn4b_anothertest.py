from cohortqn4b_another import compoundVal6Months
month_saving =  float(raw_input("Enter the monthly saving amount: "))
annual_ir = float(raw_input("Enter annual interest rate in %: "))
annual_ir = annual_ir/100
monthly_ir = float(month_saving/12)
value = round(compoundVal6Months(month_saving, annual_ir), 1)

print 'After the sixth month, the account value is %.2f' %(value)
