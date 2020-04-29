class test:
	def __init__(self):
		self.var1=[]
		self.var2=[]

	def a(self):
		self.var1.append([1,2])
		self.var2=(self.var1).copy()
		x = 56555
		self.var1= x
		return [self.var1,self.var2]


t=test()
print(t.a())