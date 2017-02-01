""" Files: Process scores: Suppose that a text file contains an unspecified number of scores.
Write a function that reads the scores from an object file and returns their total and
average. Scores are separated by blanks. Use 'scores.txt' for testing. """

#def processScores():
#    f = open('scores.txt','r')
#    scores = f.read().splitlines()
#    scores = scores.split('\r')
#
#    counter = 0
#    sum1 = 0
#
#    for x in scores:
#        x = float(x)
#
#        sum1 += x
#        counter +=1
#    average = sum1/counter
#    return average
#    return scores
#
#print processScores()
f = open('scores.txt','r')
def scores(f):
    score = f.read().splitlines()
    print score
    counter = 0
    total = 0
    for i in score:
        total+=float(i)
        counter+=1
    avg=total/counter
    return total,avg

print scores(f)