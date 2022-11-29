age=input("enter your age: ")
age=int(age)

if age==0:
    print("you can't watch")

elif 0<age<=3:
    print("Ticket price:Free")
elif 3<age<=10:
    print("Ticket price:150")
elif 10<age<=60:
    print("Ticket price:250")
else:
    print("ticket price:200")

