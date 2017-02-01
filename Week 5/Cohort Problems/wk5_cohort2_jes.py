import math
def leapYear(year):
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 != 0:
        return False
    else:
        return True

def dayOfWeekJan1(year):
    d = (1 + 5*((year-1)%4) + 4*((year-1)%100) + 6*((year-1)%400))%7
    return d

def numDaysInMonth(month_num,leap_year):
    if month_num < 8:
        if month_num%2 != 0:
            return 31
        else:
            if month_num == 2:
                if leap_year == True:
                    return 29
                else:
                    return 28
            else:
                return 30
    else:
        if month_num%2 == 0:
            return 31
        else:
            return 30

def constructCalMonth(month_num, first_day_of_month, num_days_in_month):
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_dates = []
    month_dates.append(month[month_num-1])
    date = ''
    for j in range(1,num_days_in_month+1):
        if len(date) >= 20:
            month_dates.append(date)
            date = ''
        if j == 1:
            for i in range(0,7):
                if i == first_day_of_month:
                    if i == 0:
                        date += ' '+str(j)
                    else:
                        date += '  '+str(j)

                    break
                    
                else:
                    if i == 0:
                        date += '  '
                    else:
                        date += '   '
        else:
            if len(date) <= 20 and len(date) >= 2:
                if j < 10:
                    date += '  '+str(j)
                else:
                    date += ' '+str(j)
            if len(date) < 2:
                if j < 10:
                    date += ' '+str(j)
                else:
                    date += str(j)
        if j == num_days_in_month:
            month_dates.append(date)
    return month_dates
     
def constructCalYear(year):
    cal = []
    cal.append(year)
    n = 0
    days = 0 
    for i in range(1,13):
        n = dayOfWeekJan1(year)
        if i == 1:
            pass
        else:
            days += numDaysInMonth(i-1,leapYear(year))
            n = (days-(7-n))%7
        cal.append(constructCalMonth(i, n, numDaysInMonth(i,leapYear(year))))
    return cal
    
def displayCalendar(calendar_year):
    days = ' S  M  T  W  T  F  S'
    cal = ''
    for i in range(1,13):
        j = 0
        if i != 12:
            while j < len(constructCalYear(calendar_year)[i]):
                if j == 0:
                    cal += constructCalYear(calendar_year)[i][j]
                    cal += '\n'
                    cal += days
                    cal += '\n'
                else:
                    cal += constructCalYear(calendar_year)[i][j]
                    cal += '\n'
                j += 1
            cal += '\n'
        elif i == 12:
            while j < len(constructCalYear(calendar_year)[i]):
                if j == 0:
                    cal += constructCalYear(calendar_year)[i][j]
                    cal += '\n'
                    cal += days
                    cal += '\n'
                elif j == len(constructCalYear(calendar_year)[i])-1:
                    cal += constructCalYear(calendar_year)[i][j]
                else:
                    cal += constructCalYear(calendar_year)[i][j]
                    cal += '\n'
                j += 1
    return cal
    
print displayCalendar(2016)
        
    

