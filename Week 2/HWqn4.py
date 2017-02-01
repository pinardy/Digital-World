def bmi(weight,height):
    wt_pounds = weight*0.45359237
    ht_inch = height*0.0254
    x = wt_pounds/(ht_inch)**2
    return x