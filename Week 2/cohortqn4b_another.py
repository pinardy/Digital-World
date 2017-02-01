#month_saving =  100
#annual_ir = 0.05
#monthly_ir = float(annual_ir/12)

def compoundVal6Months(month_saving, annual_ir):
    #month_saving =  100
    #annual_ir = 0.05
    monthly_ir = float(annual_ir/12)

    month_1=month_saving*(1+monthly_ir)
    month_2=(month_saving+month_1)*(1+monthly_ir)
    month_3=(month_saving+month_2)*(1+monthly_ir)
    month_4=(month_saving+month_3)*(1+monthly_ir)
    month_5=(month_saving+month_4)*(1+monthly_ir)
    month_6=(month_saving+month_5)*(1+monthly_ir)
    return month_6