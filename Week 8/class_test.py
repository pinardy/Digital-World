class A:
    x = []
    def add(self):
        self.x.append(1)
class B:
    def __init__(self):
        self.x = []
    def add(self):
        self.x.append(1)
x = A()
y = A()
x.add()
print x.x
y.add()
# print "A's x:",x.x

x = B()
y = B()
x.add()
y.add()
# print "B's x:",x.x