#def yearsDays(minutes):
#    years = minutes / 525600
#    days =  (minutes % 525600)/(60*24)
#    return years, days

from cohortqn2 import yearsDays
minutes = int(raw_input("Enter the number of minutes: "))
years,days = yearsDays(minutes)
    
print minutes, 'minutes is approximately', years, 'years and', days, 'days.'
print '%d minutes is approximately %d years and %d days.' %(minutes, years, days)