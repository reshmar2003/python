class Employee:

    company='learn2code'
    def __init__(self,name,age,salary,gender,desig,dept,resposibility,cpu,gpu,ram):   #self is a object
        #print('new object created')
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        self.email=self.generateEmail(Employee)
        self.job=Job(desig,dept,resposibility)
        self.computer=Computer(cpu,gpu,ram)

    def generateEmail(self,cls):
        return f'{self.name}@{cls.company}.com'

    
    def showInfo(self):
        print(self.name,self.age,self.gender,self.email,self.salary)

    @classmethod
    def changeCompanyName(cls,newName):
        cls.company = newName

    @staticmethod
    def info():
        print("This is a class for creating employee objecta and the it requires ")


class Job:
    def __init__(self,designation,department,resposibility):
        self.designation=designation
        self.department=department
        self.resposibility=resposibility

    def showInfo(self):
        print(self.designation,self.department,self.resposibility)


class Computer:

    def __init__(self,cpu,gpu,ram):
        self.cpu=cpu
        self.gpu=gpu
        self.ram=ram
    
    def showInfo(self):
        print(self.cpu,self.gpu,self.ram)

    

obj=Employee('John',39,'$20000','M','Manager','IT','Servers','i7','gtx',22)
obj.showInfo()
obj.job.showInfo()
obj.computer.showInfo()

