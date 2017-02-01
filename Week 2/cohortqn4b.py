#from ___ import ___
month_saving =  100
annual_ir = 0.05
monthly_ir = float(annual_ir/12)

def compoundVal6Months(month_saving, annual_ir):
    value = month_saving*(1+monthly_ir)
    month = 1 
    while month <= 6:
        value = (100 + value)*(1+monthly_ir)
        print "The value in the account in month %d  is %.2f" %(month, value)
        month += 1
        if month == 6:
            return value
    
compoundVal6Months(month_saving, annual_ir)
