class Account:
	def __init__(self,name,accNum,balance):
		self.name=name
		self.accNum=accNum
		self.balance=balance
	def deposit(self, amt):
		self.balance=self.balance+amt
	def withdraw(self, amt):
		self.balance=self.balance-amt
	def __str__(self):
		 return '%s,'%self.name + ' %s,'%self.accNum + ' balance: %s'%(str(self.balance))

a1 = Account('John Olsson', '19371554951', 20000) 
a1.withdraw(4000)
print a1

