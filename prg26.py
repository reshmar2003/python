class Employee:

    company ='Learn2code'

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

    @classmethod
    def changeCompanyName(cls,newName):
        cls.company = newName

    @staticmethod
    def info():
        print('This is a class for creating employee objecta and the it requires')
    
Employee.changeCompanyName('LLearn2code')

Employee.info()
obj=Employee('John',39,'$20000','M')

obj.showInfo()