def getDigit(number):
	if number < 10:
		return number
	else:
		num=str(number)
		output=int(num[0])+int(num[1])
		return output

def sumOfOddPlace(number):
	num_str = str(number)
	output=0
	for i in num_str[::2]:
		output+=int(i)
	return output

def prefixMatched(number,d):
	a=str(number)
	b=str(d)
	length = min(len(a),len(b))
	num=''
	for i in range(length):
		if a[i]==b[i]:
			num+= b[i]
	if num==str(d):
		return True
	else:
		return False

def getSize(d):
	return len(str(d))

def getPrefix(number,k):
	num_str=str(number)
	if len(num_str)<k:
		return number
	else:
		return num_str[0:k]

def sumOfDoubleEvenPlace(number):
	num_str=str(number)
	sumSingles=0
	for i in num_str[-2::-2]:
		double=int(i)*2
		# print double
		# print type(double)
		if len(str(double))==2:
			pass
		else:
			sumSingles+=int(double)
	return sumSingles

def isValid(number):
	if getSize(number) < 13 or getSize(number)>16:
		return False
	elif getPrefix(number,1) not in [4,5,6]:
		return False
	elif getPrefix(number,2) not in [37]:
		return False

	summ=sumOfOddPlace(number)+sumOfDoubleEvenPlace(number)
	# print summ	
	if summ%10==0:
		return True
	else:
		return False

# print isValid(4388576018402626)
# print isValid(4388576018410707)
# print isValid(371826291433349)
print isValid(5411045872559122)
# print isValid(6011432717792989)


