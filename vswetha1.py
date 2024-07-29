 '''stack=[]
stack.append('a')
stack.append('b')
stack.append('c')
print("initial stack")
print(stack)
print("\n stack after elements are popped:")
print(stack)

queue=["abi","aruna","aarthi"]
queue.append("arun")
queue.append("sri")
print(queue)
print(queue.pop(2))
print(queue)

divide_numbers=7/0
print(divide_numbers)'''
'''try:
    even_numbers=[2,3,4,5]
    print(even_numbers)
except ZeroDivisionError:
    print("denominator cannot be 0")
except IndexError:
    print("index out of bound")
'''


'''var=open("method.txt",'w')
var.write("The students are the bjbkmnb,s mfjn ,\n , the marks statement is ;the  jjkgj")
var.write("Student Name \n age \n marks \n")
var.write("swetha \t 22 \t 55")
var.close()

var=open("method.txt","r")
print(var.read())
var.close()
'''














'''
name=open("data.txt","a")
name.write("the datas are stored to condent\n")
name.write("Employee name\tsalary\tdesignationAddress\t\n")
name.write("muruga\t\t\t10000\tBEmyd\n")
name.write("livewire\t 300 \t no\t myd\t")
name.close()

name=open("data.txt","r")
print(name.read(12))


with open('data.txt') as name:
    data=name.read()
print(data) '''

'''
import os
if os.path.exists("new.py"):
    os.remove("new.py")
    print("File deleted")
else:
    print("File doesnot deleted")

class person():
    name="swetha"
    age=22
    place="myladuthurai"
obj=person()
print(obj.age)
print(obj.place)
print(obj.name)

class person:
     employeename="abinaya"
     employeename="ajay"
obj=person()
print(obj.employeename)
'''
class addition:
    first=0
    second=0
    answer=0
    def __init__(self,f,s):
     self.first=f
     self.second=s
    def display(self):
     print("first number="+str(self.first))
     print("second number="+str(self.second))
     print("addition of two numbers ="+str(self.answer))
    def calculate(self):
     self.answer=self.first+self.second
obj1=addition(100,200)
obj2=addition(20,40)
obj1.calculate()
obj2.calculate()
obj2.display()

