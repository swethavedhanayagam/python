#if statement
name=input("enter your name:")
age=input("enter your age:")
city=input("enter your city:")
std=int(input("enter your std:"))
school=input("enter your school:")
tamil=int(input("enter your tamil marks:"))
english=int(input("enter your english marks:"))
maths=int(input("enter your maths marks:"))
total=tamil+english+maths
average=total/3
print(total)
print(average)
if total>250:
    print("you got a bio")
else:
    print("you got a com")



num=int(input("enter tour number"))
if num>30:
    print("good")



num=int(input("Enter your number: "))
if num > 0:
   print("The number is positive")
else:
    print("The if statement is easy")



# if else
num=int(input("enter tour number"))
if num>0:
    print("good")
else:
    print("bad")




age=int(input("enter your age:"))
if age<18:
    print("your are eligible to vote")
else:
    print("your are not eligible to vote")

    


age=int(input("enter your age:"))
if age>25:
    print("your are eligible to election:")
else:
    print("your are  not eligible to election:")


#if  else workout
age=int(input("enter your age:"))
if(age<30):
    print("you are eligible")
else:
    print("you are not eligible")    

#elif
num=int(input("enter your number:"))
if num>30:
     print("good")
elif num==30:
    print("this is equal")
else:
    print("bad")



x=int(input("what is your exam score?"))
if x>=85:
    print("you got an A!congrats")
elif x>=75:
    print("you got a B! well done!")
elif x>50:
    print("you got a C! well done!")
elif x==5:
    print("you got a D! well done!")
else:
    print("you diid not pass the exam")    


#nestedif
num=int(input("enter your number:"))
if num>=0:
 if num==0:
        print("this is equal to 0")
 else:
    print("this is positive number")
else:
    print("this is negative number")


#nested
username=input("enter your username:")
password=input("enter your password:")
if username=="bhavya":
  if password=="livewire":
    print("login a successful!welcome admin")
  elif password=="12345":
    print("weak password.please reset your password")
  else:
    print("incorrect password.please try again")
else:
        if username=="dd":
           if password=="jan":
             print("login successful welcome dd")
           else:
             print("incorrect password please try again")
        else:
               print("unknown user.please try again")




if num>=0:
    if num==0:
        print("this is eqal to0")
    else:
        print("this is positive number")    
else:
        print("this is negative number")                   




