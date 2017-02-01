def letterGrade(mark):

    if 90 <= mark <= 100:
        return 'A'
    elif mark <= -1:
        return None
    elif 80 <= mark < 90:
        return 'B'
    elif 70 <= mark < 80:
        return 'C'
    elif 60 <= mark < 70:
        return 'D'
    elif mark < 60:
        return 'E'
    else:
        return None
    
