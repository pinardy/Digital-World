def reverse(s):
    output =''
    for i in s[::-1]:
        output = output + i
    return output
    
# def reverse(s):
#     i = len(s) - 1
#     sNew = ''
#     while  i >= 0:
#         sNew = sNew + str(s[i])
#         i = i -1
#     return sNew
    
print reverse('I am testing')
