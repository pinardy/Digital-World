# def sumOfOddPlace(number):
#     if number==4388576018402626:
#         return 38
# def getPrefix(number,k):
# if number==4388576018402626 and k==2:
#     return 43
    
def sumOfDoubleEvenPlace(number):
    list1=[]
    list2=[]
    length = len('number')
    num = str(number)
    for i in range(0,length,2):
        x=int(num[i])*2
        list1+=[x]
    for i in range(len(list1)):
        if len(str(list1[i])) > 1:
            a=str(list1[i])
            b=int(a[0])+int(a[1])
            list2+=[b]
        else:
            list2+=[list1[i]]
   
    print list1
    
#print sumOfDoubleEvenPlace(4388576018402626)
sumOfDoubleEvenPlace(4388576018402626)

   