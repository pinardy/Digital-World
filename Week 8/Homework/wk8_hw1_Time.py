class Time:
	def __init__(self,hour,minute,second):
		self.hour=hour
		self.minute=minute
		self.second=second
	def getHour(self):
		return self.hour
	def getMinute(self):
		return self.minute
	def getSecond(self):
		return self.second
	def setTime(self,elapseTime):
		self.second = elapseTime % 60  # Take remainder after dividing by 60
        self.minute = elapseTime // 60 % 60  # Take remainder after dividing by 60*60
        self.hour = elapseTime // 3600 % 12  # Take remainder after dividing by 12*60*60

# t = Time(5, 30, 23)
# ans = (t.getHour(), t.getMinute(), t.getSecond())
# print ans
# t.setTime(555550)
# ans = (t.getHour(), t.getMinute(), t.getSecond())
# print ans

thetime = Time(2, 4, 24)
thetime.setTime(55550)
print thetime.getHour(), thetime.getMinute(), thetime.getSecond()