class Employee:
	def __int__(self):
		self.name=None
		self.id=None
	
	def accept(self):
		self.name=input("Enter Name : ")
		self.id=int(input("Enter id : "))
		
	def display(self):
		print("Employee name : ",self.name)
		print("Employee id : ",self.id)
		
	
if __name__=="__main__":
	e = Employee()
	e.accept();
	e.display();
