import time
# startTime=time.time()
# time.sleep(5)
# endTime=time.time()
# elapsedTime= endTime - startTime

# print type(startTime)
class StopWatch:
	def __init__(self):
		self.startTime=time.time()
		self.endTime=-1
	def start(self):
		self.startTime=time.time()
		self.endTime=-1
	#def start(self):
	#	self.__init__()
	def getStartTime(self):
		return self.startTime
	def getEndTime(self):
		return self.endTime
	def stop(self):
		self.endTime=time.time()
	def getElapsedTime(self):
		if self.endTime==-1:
			return None
		else:
			return int(round((self.endTime-self.startTime)*(10**3)))

sw1=StopWatch()
print sw1.getElapsedTime()
print sw1.getEndTime()