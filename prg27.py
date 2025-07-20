class A:

    def __init__(self):
        print('a')

    def method1(self):
        print('Method 1')
    
    def method2(self):
        print('Method 2')

class B(A):

    def __init__(self):
        print('b')

    def method3(self):
        print('Method 3')

    def method4(self):
        print('Method 4')

class C(B):

    def __init__(self):
        print('c')

    def method5(self):
        print('Method 5')

a=A()
b=B()
c=C()

a.method1()
a.method2()

b.method1()
b.method2()
b.method3()
b.method4()

c.method1()
c.method2()
c.method3()
c.method4()
c.method5()
