class Employee:
    def __init__(self,name,age,salary,gender):   #self is a object
        #print('new object created')
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        self.email=self.generateEmail()

    def generateEmail(self):
        return f'{self.name}@company.com'

    def showInfo(self):
        print(self.name,self.age,self.gender,self.email,self.salary)


obj=Employee('John',39,'$20000','M')
obj.showInfo()
#obj=Employee()
#obj=Employee()
#obj=Employee()