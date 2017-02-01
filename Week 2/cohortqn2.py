def yearsDays(minutes):
    years = minutes / 525600
    days =  (minutes % 525600)/(60*24)
    return years, days