import math

def leapYear(year):
    if year%4!=0:
        return False
    elif year%100!=0:
        return True
    elif year%400!=0:
        return False
    else:
        return True

def dayOfWeekJan1(year): # 0-Sunday,1-Monday,...,6-Saturday
    return (1+(5*((year-1)%4))+(4*((year-1)%100))+(6*((year-1)%400)))%7
    
def numDaysInMonth(month_num,leap_year):
    if month_num==1 or month_num==3 or month_num==5 or month_num==7 or month_num==8 or month_num==10 or month_num==12:
        return 31
    elif month_num==4 or month_num==6 or month_num==9 or month_num==11:
        return 30
    elif month_num==2:
        if leap_year:
            return 29
        else:
            return 28
    else:
        return None    

def constructCalMonth(month_num, first_day_of_month, num_days_in_month):
    result = []
    if month_num==1:
        result.append("January");
    elif month_num==2:
        result.append("February");
    elif month_num==3:
        result.append("March");
    elif month_num==4:
        result.append("April");
    elif month_num==5:
        result.append("May");
    elif month_num==6:
        result.append("June");
    elif month_num==7:
        result.append("July");
    elif month_num==8:
        result.append("August");
    elif month_num==9:
        result.append("September");
    elif month_num==10:
        result.append("October");
    elif month_num==11:
        result.append("November");
    elif month_num==12:
        result.append("December");
        
    line = ""
    counter = first_day_of_month # counts days of the week
    
    for i in range(counter):
        line+="   " # 2x spaces for each missing date, and 1x spacing formatting
    
    for i in range(num_days_in_month):
            line+="%2d" % (i+1) # add the date
            line+=" " # add a space between dates
            counter+=1
            if counter == 7: # end of the line
                result.append(line[:-1]) # append without last spacing
                line="" # reset line
                counter=0 # reset day counter
                
    if line!="": # if last line still has some dates not appended
        if line[-1]==' ': # if there is an extra space at the end of the line
            line=line[:-1] # get rid of last spacing
        result.append(line)
    
    return result
        
def constructCalYear(year):
    result=[year]
    for i in range(12):
        first_day_of_month=dayOfWeekJan1(year)
        for j in range(i):
            first_day_of_month+=numDaysInMonth(j+1,leapYear(year))
        first_day_of_month=first_day_of_month%7
        result.append(constructCalMonth(i+1,first_day_of_month,numDaysInMonth(i+1,leapYear(year))))
    return result


def displayCalendar(calendar_year):
    retVal=''
    yearCalendar=constructCalYear(calendar_year)
    month_num=1
    for i in range(12):
        monthCal=yearCalendar[month_num]
        retVal+=monthCal[0]+'\n'
        retVal+=" S  M  T  W  T  F  S\n"
        for lines in monthCal[1:]:
            retVal+=lines+'\n'
        retVal+='\n'
        month_num+=1
    retVal=retVal[:-2]
    return retVal