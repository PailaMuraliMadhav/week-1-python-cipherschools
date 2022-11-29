#print function
print("hello world")
print('hello world')
print("hello\"world\"world")
#escape sequence
print("lineA\nlineB")
#print("lineA\nlineB\nlineC") #\n is for new line
print("this is double backslash\\\\")
print("name\tmurali")
print("mura\bali")
#comments
#ctrl+/

#escape characters as normal text
#output:  lineA \n lineB
print("lineA \\n lineB")


#execise
print("this is \\\\ double backslash")
print("these are \/\/\/\/\ mountains")
print("he is\tawesome")
print("\\\" \\n \\t \\\'" )

#raw string
print(r"lineA\"line B")#r is used to not treat any escape sequence

#emoji
#print("\U0001F60")unicode.org/emoji

#calculator
print(2+3)
print(2/4)#floating  div
print(4//2)
print(2//4)#interger div
print(2**3)#exponent
print(round(2**0.5,4))
print(3%2)#remainder
print((2+3)*2)
 
#variable
number1=2
print(number1)
number1=4
print(number1)
#string,number
name="murali"
print(name)
# number is not used in the starting
# it can be used in the middle of the code 
#special number is not at all used in the code
user_one_name="rohit" #snake case writing
print(user_one_name)
userOneName="murali"#camel case writing"
print(userOneName)

#user input function
name=input("type your name")
print("hello "+ name)
#string
age=input("what is your age ?")
print("your age is "+age)

#string(collection of char inside singelor double quotes)
first_name="paila"
last_name="Murali"
full_name=first_name+" "+last_name
print(full_name)
print(first_name+"3")
#print(first_name+3)error
print(first_name*3)

#integer(int)
a=int(input("enter first number"))
b=int(input("enter second number"))
total=a+b
#print("total is"+str(total))

#str
#4---"4"
 #int
#"4"-->4
#float
#4--->4.0
num1=str(4)
num2=float("44")
num3=int(3)
print(num1+num3)
#more string
num,age="murali",18
print("hello"+name+"your age is"+age)
x=y=z=1
print(x+y+z)
 #two or more input in one line
name,age=input("enter your name and age").split()
print(name)
print(age)

#exercise 2
a=input("enter the first number:")
b=input("enter the second number:")
c=input("enter the third number:")
a,b,c=input("enter the three number comma seperated:")






