#string indexing
language="python"
#p=0,-6
#y=1,-5
#t=2,-4
#h=3,-3
#o=4,-2
#n=5,-1
print(language[4])
print(language[2])
print(language[-4])

#string slicing/selecting sub sequences
lang="python"
print(lang[1:3])
print(lang[-1:-3])
print(lang[0:5])
print(lang[:6])
print(lang[0:6])
print(lang[1:])
print(lang[-3:6])

#string argument
lang="python"
print(lang[0:5:2])#leave one word after one
print(lang[0::3])
print(lang[5::-1])
print(lang[::-1])

#exercis  3
a=input("enter your name:")
print(f"reverse of your name {a[::-1]}")

#string methods
#len function
a="Muralipaila"
print(len(a))
#lower
print(a.lower())
#upper
print(a.upper())
#count
print(a.title())
#count
print(a.count("a"))

#exercise 3
name,char =input("enter comma seperated name and character:").split(",")
print(f"length of you name is{len(name)}")
print(f"character count:{name.count(char.lower())}")#case sensitive

#solve problem with spaces using strip method
a="    murali    "
b=".............."
print(a,b)
print(name.lstrip()+b)
print(name.rstrip()+b)
print(name.strip()+b)
print(a.replace(" ",""))

#find and replce
#replace
string="he is handsome and good player"
print(string.replace("is","was"))
#find
print(string.find("and"))


#string is imutable
a="string"
a.replace('t','T')
print(a)
#assignment operators
a="murali"
name+="it"
print(name)
age=17
age+=2
print(age)

#if statement in python
age=input("enter your age: ")
age=int(age)
if age >=14:
    print("your age above 14")
else:
    print("you are below 14")

#CH-3 exercise
a=27
b=input("guess a number b/w 1 and 100: ")
b=int(b)
if b==a:
    print("You win!!")
else:
    if b<1:
        print("too low")
    else:
        print("too high")




