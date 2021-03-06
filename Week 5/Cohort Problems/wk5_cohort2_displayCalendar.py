import math
def leapYear(year):  # True: leap year # False: not leap year
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm 
    
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 !=0:
        return False
    else:
        return True

def dayOfWeekJan1(year):
# http://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Gauss.27_algorithm
#    d = R(1 + 5R(A-1,4) + 4R(A-1,100) + 6R(A-1,400),7)
#    d = R(1 + 5M + 4N + 6Q, 7)

    M = (year-1)%4
    N = (year-1)%100
    Q = (year-1)%400
    P = 1 + 5*M + 4*N + 6*Q
    d = P%7
    return d # d ranges from 0 to 6 (Sun:0, Mon:1, etc.)        
    
def numDaysInMonth(month_num,leap_year):
    num_of_days_in_month={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31,
    8:31, 9:30, 10:31, 11:30, 12:31}  
        
#better to use dict rather than multiple if statements for each month

    if month_num==2 and leap_year:
        return 29
    else:
        return num_of_days_in_month[month_num]

def constructCalMonth(month_num, first_day_of_month, num_days_in_month):
    mthdict={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',
    8:'August',9:'September',10:'October',11:'November',12:'December'}    
    
    output=[mthdict[month_num]]
    week='   '*first_day_of_month  #+'1'
    #print week
    #print '1234567890123456'
    date=1
    day=first_day_of_month
    while date<num_days_in_month:
        while day<=6 and date<=num_days_in_month :
            week+='%3s'%date  # %3s puts 3 spaces 
            date+=1
            day+=1
            #if date>c:
                #break  #to prevent >31 day on calendar

        output.append(week[1:]) #slicing the list (read from 1 onwards)
        #print week
        week='' #resetting string 
        day=0  #setting day back to sunday
    return output


def constructCalYear(year):
    output=[str(year)]
    firstDay=dayOfWeekJan1(year)
    leap_year=leapYear(year)
    #print firstDay
    for mth_num in range(1,13):
        n_d_m=numDaysInMonth(mth_num, leap_year)
        #print mth_num, n_d_m
        mth_list=constructCalMonth(mth_num, firstDay, n_d_m)
        #print mth_list
        firstDay=(firstDay+n_d_m)%7  #getting 1st day of next month
        output.append(mth_list)
    return output

def displayCalendar(year):
    output=''
    yearList=constructCalYear(year)
    #print yearList
    for mth_list in yearList[1:]:
    #for mth_list in yearList:
        print mth_list
        output+='\n'+mth_list[0]+'\n'
        output+=' S  M  T  W  T  F  S\n'
        #print output
        for week in mth_list[1:]:
            #print week 
            output+=week+'\n'
        return output
    #return output[1:-1]
    

#print 'Start'
displayCalendar(2015)
#print 'End'
    