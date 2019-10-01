max = 5
class SelectionSort:
	a=[]
	def __int__(self):
		self.a=[]
		self.size = 0
		
	def accept(self):
		self.size=int(input("Enter Size : "))
		for i in range(0,self.size):
			self.a.append(int(input("Enter Data : ")))
		
	def display(self):
		print(self.a)
	
	def sort(self):
		min_index=0;
		for i in range(0,self.size):
			min_index = i;
			for j in range(i+1,self.size):
				if self.a[min_index] > self.a[j] :
					min_index = j
				
			#self.swap(self.a[min_index],self.a[i])
			temp = self.a[min_index]
			self.a[min_index] = self.a[i]
			self.a[i] = temp
	'''def swap(self,a,b):
		temp = a
		a = b
		b = temp'''
		
		
if __name__=="__main__":
	s = SelectionSort()
	s.accept()
	s.display()
	s.sort()
	s.display()
	




