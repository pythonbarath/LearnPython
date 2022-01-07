#Learn Python in Most  Simplest way & Quick Way 

# print("hi")
# print('hi')

# print(5+10)
# print(5*10)
# print(5+10*5) #BODMAS 
# print((5+10)*5)
# print(100/3)
# print(100-3)
# print(100//3) #Round off the Quotient
# print(2*3) #Multiplication
# print(2**3) #PowerOff 2^3

# print(10%3) #REMINDER
# print(100%7)
# print(100%9)
# print(100%2)

# print(2**3+2*3) #8+6
# print((2**3)+2*3)
# print((2**3+2)*3)

#Identifiers = variable= Reference Variable
# doorno = 15
# print(doorno)

#Identifiers Rules No Space Allowed 
#Shouldnot start with Numbers
# tamil1=90
# print(tamil1)
# Tamil_1=90
# print(Tamil_1)
# _TAMIL=90  #private variable is a oops concept
# print(_TAMIL)
# ##ERROR#####
# 2Tamil=90 
# print(2Tamil)

# _math=90 
# print(_math) 

#RULES 
#NO SPECIAL ALLOWED
#NO SPACE 
#UNDERSCORE ALLOWED
#NUMBER ALLOWED BUT SHOULD NOT START WITH It
#CASE Sensitive
#THERE ARE LIST OF RESERVED WORDS
#_,__STARTING -> PRIVATE Variable
#MAGIC METHODS--> __ADD__  FRONT AND BACK UNDERSCORE ALREADY DEFINED IN Python

#python Reserved words
# 33 reserved words
# import keyword
# print(keyword.kwlist)

# ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#DATATYPES

#simple and dynamically typed
#DUCK TYPING Language
# no =10 #int 
# result = False  #boolean  
#  we never mention datatypes before variable (identifiers) in python 



# Datatypes list  : 14 datatypes

# int
# float
# boolean
# complex
# bytearray
# bytes
# range
# list
# array
# tuple
# dict
# None
# set 
# frozen set 

# n = 10   #10 is pararmeter/argument
# print(type(n))  #print is function/method
# why output is class?
# all datatype is class -we will cover in oops concept

#ID - Address

# n = 10   #10 is pararmeter/argument
# print(type(n))
# print(id(n))

# a = 20   #10 is pararmeter/argument
# print(type(a))
# print(id(a))

#Search for built in function and try it
#id
#len 
#round


#########################     2HOURS COMPLETED  ##############

#INT DATATYPES

#DECIMAL Form
#BINARY Form - 0'S AND 1'S
#OCTAL Form - BASSE 8  0 to 7  start with zero and o
#HEXADECIMAL FORM  start with zero and X

# no = 0B0101
# print(no)

# no1= 0b01001   
# print(no1)


#octal 
# no = 0o776
# print(no)

# no1= 0o765
# print(no1)

#HEXADECIAMAL 

# no = 0X12
# print(no)

# no1= 0XAD
# print(no1)

#if you note all output are normal form that is decimal form

#check inbuild function for conversation

# no1= bin(20)
# print(no1)
# no1= oct(20)
# print(no1)
# no1= hex(20)
# print(no1)

#Float Datatype

#float - . 
#int 

# no = 1.23456789
# print(type(no))

# no = 1.23456789
# print(type(no))

# no = 1.2E3
# print(type(no))

# no = 1.2E7  #Exponential 2POWER 7
# print(type(no))

# COMPLEX

# a+bj

# no = 5+10j
# print((no))
# print(type(no))

# no2 = 5+10j
# total = no+no2
# print((total))
# print(type(total))

# print(no2.real)
# print(no.imag)


#Boolean #Comparison 

# no1 = 10
# no2 = 20
# print(no1>no2)
# print(no1<no2)
# print(no1==no2)
# print(no1!=no2)

# a = True
# print(a)
# print(type(a))

# print(True+True)
# print(True+False)
# print(False+False)

# no1 = "two"
# no2 = "three"
# print(no1>no2)
# print(no1<no2)
# print(no1==no2)
# print(no1!=no2)


#String

# name = "Barath"
# print(name)
# print(id(name))

# name = 'Barath'
# print(name)
# print(id(name))

# name = """ Barath's address is chennai ... he said "hi" """
# print(name)
# name = '''Barath's address is chennai ... he said "hi" '''
# print(name)

# name = '''Kolathur
#           chennai
#         anna nagar
#         tamilnadu '''
# print(name)


# name = "barath"
# city = 'chennai'
# print(name+city)
# print(name,city)  # , will add space  


# name = "barath"
# pin = 600028
# print(name,pin)
# print(name+pin)   # + BOTH SHOULD BE STRING  


#sTRING sLICING
 
# name = "barath"
# print(name[0]) #0 is the index  stars 0 and negative index stat from -1
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[-1])
# print(name[-2])

#Task print last letter and first letter

# name = "barath"
#        #012345
# print(name[0:3])
# print(name[3:])
# print(name[3:5])
# print(name[8:]) #empty 
# print(name[:5])

# a = "HAD LEARNED BASIC KNOWLEDGE OF PYTHON AND ITS FRAMEWORK LIKE DJANGO,FLASK FOR ADVANCEMENT OF SKILLS"
# print(a.title())

# name = 'abcdefghijklmnopqrstuvwxyz'
       #01234567890123456789012345

# print(name[0:5])
# print(name[-1:]) #left to right 
# print(name[5:10])
# print(name[-5:-1]) #Step operator 

#Slicing [::]

# print(name[::])
# print(name[1:10])
# print(name[1:10:2]) #positive index -1 
# print(name[10:2])  #empty set - only left to right 
# print(name[10:2:-1])  #negative index +1 
# print(name[-26:26])
# print(name[26:-1:4])


# name= "123456789"
# name2 = "123456789"

# print(len(name))  #len function doenot count Zero
# val = len(name)
# # print(name[-val:val])

# print(name[val:0:-1]) #to print in reverse #wont work

# print(name[(val-1):0:-1]) #wont work

# print(name[::])
# print(name[::-1]) #to print in reverse
# print(name[0:-5])
# print(name[10:0:-1])
# print(name[::2])


#check whether it is palindrome or not?

# name = "sun"

# print(name)

# name2 = name[::-1]
# print(name2)
# print(name==name2)

# print(name*3)  
# print(name+3) #Error


#TYPE Casting

# no = 99.45  #chaning float to int is type casting

# print(int(no))


#can we able to change name to int? 
#NOOOOOO!!!!

# name = "barath"
# print(int(name))  #VALUEERROR 

# print(float(10))
# print(float(True))
# print(float(False))

# 
# door = "10"

# print(door)
# print(type(door))
# print(int(door))
# print(type(int(door)))



#COMPLEX 

# print(complex(10))
# print(complex(5.4))
# print(complex(True))   #True part
# print(complex(False)) #imaginary
# print(complex("12"))  
# print(complex("12.7"))
# print(complex(10,20))
# print(complex(True,False))

#bool  True False  
# print(bool(0))
# print(bool(1))
# print(bool(1.5))  #Complete Zero False
# print(bool(0.3))
# print(bool(0.0))
# print(bool(5+4j))
# print(bool(0+2j))
# print(bool(0+0j))
# print(bool("True"))
# print(bool("False"))  #String always True
# print(bool(""))  #Empty string with no sapce False 
# print(bool(" "))  #Space False

#STR 
# print(str(10))  
# # print("Price is "+10)  
# print(str("Price is "+str(10))) 
# print(str("Price is "+"10"))  

# a= str(34.5)
# print(type(a))

# print(str("True"))
# print(str("False")) 

#14 DATA TYPES- 5 FUNDAMENTAL  DATA TYPES  

#ALL Fundamental Data TypeS ARE IMMUTABLE 
#integers, floats, booleans and strings. -fundamental data Type

#immutable -not changabale


# immutable example 
# no =10 

# no2 =10  #it will show the same address 

# print(id(no))
# print(id(no2))
# no2=20 

# print(id(no2))   

# once we change the value of identifier belonging to fundamental
# datatypes it wont get changed.. a new address will be created 

#IS  will check whterh the both identifier has same address

# no1 =10
# no2 =10

# print(no1 is no2)

# no1 =10
# print(id(no1))
# no2 =10.0
# print(id(no2))

# print(no1 == no2) #Equality operator
# print(no1 is no2) #Identity Operator
# print(no1 is not no2)

#BYTES 

# values = [90,80,30,40,400] #Bytes value should be below 256 
# values = [10,20,30,40]
# print(values)
# values[0]=20   #List is mutable but once converted to byte cannot mutable
# print(values)
# values = bytes(values)
# print(values)
# print(type(values))  #bytes value cannot be seen 
#                      #to view value use index        
# print(values[0])
# print(values[1])
# print(values[2])
# print(values[3])

# print(values[-1])
# print(values[-2])


# to view all values we use loops:

# for x in values:
#        print(x)

#wecannot change the value

# values[0]=92  #we will get error 

#how to get total value in the list?

# values = [10,20,30,40]
# print(values)

# total = 0
# for x in values:
#        print(x)
#        total = total +x 
#        print("total + x =  ",total)

# print(total)



#ODD Even

# No = int(input("Enter the Value "))  #change input to int or it will be string 
# print(No)
# print(type(No))

# print(int(No)+5)

# No = int(input("Enter the Value ")) 
# if No%2==0:
#        print("Even Number ")
# else:
#        print("Odd No ")


# values = [10,20,30,40,15]

# for x in values:
#        if x%2==0:

#               print("Even Number ")              
#        else:
#               print("Odd No ")

# No = int(input("Enter the Value ")) 
# if No%2==0:
#        print("Even Number ")
# else:
#        print("Odd No ")


#Operators

# Relational Operator :

# > >= < <= 

# Equality Operator

# == !=


# name1 = 'kannan'
# name2 = 'kumara'   #Lexicographical order -dicitonary order  
#                    #  a is smaller than B .B is smaller than C       
# print(name1>name2)
# print(name2>name1)
# print(name1==name2)
# print(name1!=name2)


#Escape Character 

# print("Hi Hello")
# print("Hi \t Hello") #Tab Space
# print("Hi\n Hello ")  #New Line
# print('I\'m fine ')
# print('''I'm fine''')


#Constants 

#USE CAPITAL LETTER

# MAX= 3


#Assignment operator

#+= -= *= /= //= 
# %= **= 


# no = 10
# no = no+10  
# print(no)

# # no+=1  ==>  no = no+1 

# no *= 2
# print(no)

# no **= 2
# print(no)


#Ternary Operator  (Conditional Operator)

# a=1,b=20,c=30   #ERROR OCCUR WONT SUPPORT MULTIPLE INPUT
# print(a)

# a,b,c,d = 10,20,30,40

# print(a,b,c,d)
# print(a)

# a,b,c,d = 10,20,30,40

# e = 50 if a<b else 60   #Ternary Operator consists of multiple opeartons
# print(e)


#MEMBERSHIP OPERATOR 

#in, not in 

# a = 'Today is friday'

# print('o' in a)  #checks o is available in sentence or not 
# print('f' not in a) 
# print('z' in a) 
# print('Today' in a) 

#Operator Chaining

# print(100<200)
# print(200<300)
# print(100<500<300)

#Bitwise OPerator  #No use in normal programming only used in advanced data science topics

# runtime : 4:30 
# & | ^ ~ >> <<

# & - AND na multiple pannanum

# | or symbol should ADD the value 

# ^ XOR  SAME VALUE RESULT 0 - DIFF VALUE NA 1 

# print(4&5)
# print(4|5)
# print(4^5)  

# print(bin(4)) #0100
# print(bin(5)) #0101
# print(bin(10)) #1010

# ~1010 => -(1010+1) => -(1011)=> 2**3+2**2+2**1+2**0=> 8+0+2+1=-(11)

# print(~no)

# print(10<<2)  





#Logical Operators

#AND OR NOT  

# print( 5 and 5)  #low value will be considered 

# print( 5 and 3)

# print( 5 or 3)  #first value will be taken or  high value 
# print( 4 or 6)



# result = True
# result2 = not result

# print(result)
# print(result2)


#MODULES

#PYTHON FILE - MODULES
#INSIDE MODULE IT HAS FUNCTIONS,VARIABLE ETC  


# print('hi') #Print is a module  

# we can write a Module

#For example:

#first write function and call it 

#FINDING BIGGEST VALUE 

# def big(no1,no2): #function definition 
#        if no1>no2:
#               print(no1, "is greater")
#        else:
#               print(no2, "is greater")
       

# no1 = int(input("Enter no1 : "))
# no2 = int(input("Enter no1 : "))
# big(no1,no2)  #Function calling  #no1,no2 are argument 

#the big (no1,no2) value alone goes to def big() so we can also
#write it as def big(a,b)

#PASS 

# def big(no1,no2): 
#        pass          #No OUTPUT WILL COME.. IT IS USED TO DEFINE LATER OR LOGIC NOT DISCUSSED
       

# no1 = int(input("Enter no1 : "))
# no2 = int(input("Enter no1 : "))
# big(no1,no2)


#How to use other created Modules  

# the  Above finding the biggest value can be created as module 
#by saving it in a seperate file 


#format1 

# import one 

# one.big

#format2
# import one 
# no1 = int(input("Enter no1 : "))
# no2 = int(input("Enter no1 : "))
# one.big(no1,no2)  

#the calling will pass only the value of the argument 


#Build in Modules


#CMD -> PYTHON -> help('modules')
#clear()

#MATH Module

# import math
# print(math.sqrt(100))
# print(math.pi)
# print(math.ceil(5.3))
# print(math.floor(5.3))

# from  math import *
# print(sqrt(100))
# print(pi)
# print(ceil(5.3))
# print(floor(5.3))


# eval()
#it is used to cobvet to math function

# a = input("enter the value  ")  #always stoer ad string
# print('first',a)
# print(a)
# print(type(a))
# a = eval(a)
# print('second',a)
# print(a)
# print(type(a))

#Command line arguments

# from sys import argv 

# print(argv[0])
# print(argv[1])
# print(argv[2])
# print(argv[3])
# print(argv)
# print(type(argv))

# print(int(argv[1])+int(argv[2]))
# print(int(argv[1])*int(argv[2]))
# python payilagam.py 2 4 5 6 7


#in java 

# no1=10,no2=10


#in python
# no1,no2=10,20

# no1,no2,no3,no4,no5=10,20,30,40,50
# print(no1,no2,no3,no4,no5, sep=":")
# print(no1,no2,no3,no4,no5, end="/")


# use of END

# print("Barath")
# print("chennai")

# print("Barath", end=" ")
# print("chennai")

# print("Barath", end="/")
# print("chennai")


#FORMATTED STRINGS 


#%i, %d, %f , %s 

#%s-%s operator is put where the string is to be specified
#%d operator is used as a placeholder to specify integer values
#%d stands for decimal and %i for integer.
# %f (of float) is to replace a float,

# no1,no2,no3  = 10.20,20,30
# print("no1 value %d" %no1)
# print("no2 value %i" %no2)

# name = "vignesh"

# print("Hi", name)
# print("Hi %s" %name)

# print("no1 value is  %d and no2 value is %d" %(no1,no2))
# print("no1 value is  %f and no2 value is %d" %(no1,no2))



#Replacement 

# name = 'Raja'
# city = 'chennai'
# accno = 1234
# print("Hi",name,"you are from ",city,"and your bank accnt no is ",accno)

# #For DB 
# print("Hi",name,"you are from ",city,"and your bank accnt no is ",accno)

# print("Hi {0} you are from {1} and your bank accnt no is {2} ".format(name,city,accno))

# print("Hi {a} you are from {b} and your bank accnt no is {c} ".format(a= name,b= city,c =accno))


# print("Hi {} you are from {} and your bank accnt no is {} ".format(name,city,accno))


#{} - place holder



#WAP  GRADE SYSTEM TO STUDENTS 

#>90 A+   80>A  70 B+  60- B <60 ->C

# from math import *

# mark = float(input("Enter The Mark :"))
# mark = ceil(mark)

# if mark >=90:
#        print("The Student Mark is %d  Grade is A+" %(mark))
# elif mark >=80:
#        print("The Student Mark is %d  Grade is A" %(mark))
# elif mark >=70:
#        print("The Student Mark is %d  Grade is B+" %(mark))
# elif mark >=60:
#        print("The Student Mark is %d  Grade is B" %(mark))
# else:
#        print("The Student Mark is %d Grade is C" %(mark))



# name = input("what is your name    ")
# if name == "barath":
#        print("Hi")
# print("Hello")


#WAP - TO FIND GREATEST NUMBER

# no1 = int(input("Enter No1:  ")) #80
# no2 = int(input("Enter No2:  "))#90
# no3 = int(input("Enter No3:  ")) #100

# if no1>no2:  #80>90 -false 
#        if no1>no3:
#               print("No1 is Greatest")
# elif no2>no1: #90>80 - True  
#        if no2>no3:
#               print("No2 is Greatest ")
# elif no3>no1:
#        if no3>no2:
#               print("No3 is Greatest")


#BUG IN THE ABOVE PROGRAM  






# no1 = int(input("Enter No1:  ")) #80
# no2 = int(input("Enter No2:  "))#90
# no3 = int(input("Enter No3:  ")) #100


# if no1>no2 and no1>no3:     
#        print("No1 is Greatest value is  - %d" %(no1))
# elif no2>no3:
#        print("No2 is Greatest value is - %d" %(no2))
# else:       
#        print("No3 is Greatest value is -  %d" %(no3))


#WAP TO FIND OD OR Even


# no1 = int(input("Enter No1:  ")) #80

# if no1%2 == 0:
#        print("Even")
# else:
#        print("Odd")



#Iterative #reperative input  we use While  & Break 




# mind = 7

# while True:
#        guess = int(input("Enter your numb between 1 and 10 :     "))
#        if guess == mind:
#               print("Your Guess is correct")
#               break
#        elif guess > mind:
#               print(" Your Guess is too high")
#        elif guess < mind:
#               print(" Your Guess is too low") 

     

#WAP -LIKE 1 2 3 4 5 

#format  1

# print(1, end = ' ')
# print(2, end = ' ')
# print(3, end = ' ')
# print(4, end = ' ')
# print(5, end = ' ')

#format  2
#visit the link below 
# https://i.ibb.co/cXxZjcW/vlcsnap-2021-12-19-16h36m45s477.png



#Additon Short form is multiplication 
#multiple IF statement -> While Loop 
# if if if    -> while  


#IF, ELIF, and ELSE are Statements  

#While ,Doehile ,for -loops

# count = 1
# while count <= 5:
#        print(count,end=' ')
#        count = count+1


#print in reverse

# count = 100
# while count >= 1:
#        print(count,end=' ')
#        count = count-1



#print till 100 and break after 5 counts 

#like 

# count = 50
# while count >= 1:
#        if count%5==0:
#               print()   #Normal print() will always print in new line 
#        print(count,end=' ')  #else is not complusary we can use else 
#        # count = count-1
#        count -= 1





#PRINT ONLY EVEN NUMBER 

# count = 1
# max = int(input("Enter the Value:   "))
# while count <= max:
#        if count %2 == 0:            
#               print(count,end = " ")       
#        count += 1




#PRINT ONLY ODD  NUMBER 

# count = 1
# max = int(input("Enter the Value:   "))
# while count <= max:
#        if count %2 != 0:            
#               print(count,end = " ")       
#        count += 1

#format 2 


# count = 1
# max = int(input("Enter the Value:   "))
# while count <= max:
#        if not  count %2 == 0:            
#               print(count,end = " ")       
#        count += 1


#WAP FOR MULTIPLES OF THREE  

# count = 1
# user = int(input("Enter the Range:  "))
# while count <= user:
#        if count %3 == 0:
#               print(count, end= " ")
#        count += 1

#mutual multiplies of 3 and 4 

# count = 1
# user = int(input("Enter the Range:  "))
# while count <= user:
#        if count %3 == 0 and count %4 == 0 :          
#               print(count, end= " ")
#        count += 1


# count = 1
# user = int(input("Enter the Range:  "))
# while count <= user:
#        if not count %3 == 0 and count %4 == 0 :          
#               print(count, end= " ")
#        count += 1


#video - timing - 6:28:40

# count = 1
# user = int(input("Enter the Range:  "))
# while count <= user:
#        if not (count %3 == 0 and count %4 == 0):          #12 and 24 will be missing  
#               print(count, end= " ")
#        count += 1


#Finding Multiplies of 3 in different method 

# count = 3
# user = int(input("Enter the Range:  "))
# while count <= user:
#        print(count, end= " ")
#        count += 3


# why we are using loops?
# to do a similar action for a n numnber of time


#eg1 
# total = 0
# total =total +1 
# total =total +2
# total =total +3 
# total =total +4 


#eg2
# total = 0
# no =1 
# total =total +no 
# no +=1 
# total =total +no
# no +=1 
# total =total +no
# no +=1 
# total =total +no
# no +=1 

#eg3 


# total = 0
# no = 1 
# while no<=5:
#        total = total + no 
#        no +=1
# print(total) 

#Addition of first N numbers 


# total = 0 
# no = 1
# user = int(input("Enter the Number: "))
# while no <= user:
#        total = total+no
#        no += 1
       

# print(total)



#Multiple of first N numbers 


# total = 1
# no = 1
# user = int(input("Enter the Number: "))
# while no <= user:
#        total = total*no
#        no += 1
       

# print(total)


#Break & Continue

# no =1

# while no<=10:
#        print(no, end=" ")
#        if no == 5:              
#               break
#        no+=1

# no =1

# while no<=10:       
#        if no == 5:
#               no+=1   #no 5 wont be there it will get added                          
#               continue
#        print(no)
#        no+=1                            


# name = ''
# while not name == "barath":
#        name = input("What is your name? ")


# name = ' '
# while True:

#        if name == "barath":
#               print("WELCOME Barath ")
#               break
#        else:

#               name = input("What is your name? ")


# REF

# mind = 7

# while True:
#        guess = int(input("Enter your numb between 1 and 10 :     "))
#        if guess == mind:
#               print("Your Guess is correct")
#               break
#        elif guess > mind:
#               print(" Your Guess is too high")
#        elif guess < mind:
#               print(" Your Guess is too low") 


#WAP TO PRINT THE INPUT CHARACTER :
# name = input("What is your name? ")
# length = len(name)
# i = 0 
# while i<length:
#        print(name[i])
#        i+=1


#In Function 

#WAP TO CHECK WHTER THE INPUT HAS THE SAME WORD IN LIST
# name = input("What is your name? ")
# length = len(name)
# i = 0 
# while i<length:
#        if name[i] in ['a','e','i','o','u']:
#               print(name[i])
#        i+=1


#count NO of vowels present in name 

# name = input("What is your name? ")
# length = len(name)
# i = 0 
# count = 0
# while i<length:
#        if name[i] in ['a','e','i','o','u']:
#               print(name[i])
#               count += 1
#        i+=1
# print("The total no of vowels is ", count)



#print only number from given input 
#AND IS EQUAL = TO

# email  = input("What is your name? ")
# length = len(email)
# i = 0 
# count = 0
# while i<length:
#        if email[i] >='0' and email[i] <='9':
#               print(email[i])
#               count += 1
#        i+=1
# print("The total Number count  is ", count)


#print only alphabet  from given input 

# email  = input("What is your name? ")
# length = len(email)
# i = 0 
# count = 0
# while i<length:
#        if email[i] >='a' and email[i] <='z':
#               print(email[i])
#               count += 1
#        i+=1
# print("The total Number alphabet   is ", count)


#Print Multiples of 6


# no =1

# while no<=12:
#        print(no*6)
#        no+=1

# Print it in tables format 



# no =1

# while no<=12:
#        print("6  * %i  = %i" %(no,no*6))
#        no+=1


#WAP to get repeated input until stop 

# format 1

# choice = " "
# total = 0

# while not choice  == "stop":
#        mark = int(input("Enter the Mark:   "))            
#        total = total + mark
#        choice = input("Type stop to stop: ")
       
# else:       
#        print(total)




#Format2


# choice = " "
# total = 0
# mark = 0
# while not choice  == "stop":
#        mark = input("Enter the Mark:   ")
#        if mark == "stop":
#               break
#        else:
#               mark = int(mark)
#               total = total + mark
#               print(total)


#everyloop has else 
#if else 
#while- else
#for-else 

#WAP to find the divisors

# 120

#logic 

# if 120% 2 ==0:
#        print(2)

# elif 120% 3 ==0:
#        print(3) 
# elif 120% 4 ==0:
#        print(4) 

#Multiple IF STATEMENT CAN BE CHANGED INTO Loop


# no = 120
# div =2

# while div <no:
#        if no % div == 0:
#               print(div)
#        div += 1

#WAP to find COMMON DIVISORS OF TWO NUMBER AND TAKE INPUT FROM USERS 


# no1,no2 = int(input("Enter the Number:")),int(input("Enter the Number:"))
# no1,no2 = map(int,input("Enter the Number:").split(","))
# div =2
# if no1<no2:
#        small = no1
# elif no2<no1:
#        small = no2
# while div <small:
#        if no1 % div == 0 and no2 % div == 0:
#               print(div)
#        div += 1

#WAP to find  LAST COMMON DIVISORS OF TWO NUMBER AND TAKE INPUT FROM USERS 
# no1,no2 = map(int,input("Enter the Number:").split(","))
# div =2
# if no1<no2:
#        small = no1
# elif no2<no1:
#        small = no2
# while div <small:
#        if no1 % div == 0 and no2 % div == 0:
#               last = div
#        div += 1
# else:
#        print("Last Divisor(GCD): ",last)

#format 2

# import math

# print("GCD of ", math.gcd(120,200))

#ternary operator 

# eg1  we are going to simplify from  1348 to 1351 line 

# no1,no2 = map(int,input("Enter the Number:").split(","))
# div =2
# if no1<no2:
#        small = no1
# elif no2<no1:
#        small = no2
# while div <small:
#        if no1 % div == 0 and no2 % div == 0:
#               last = div
#        div += 1
# else:
#        print("Last Divisor(GCD): ",last)



#eg 

# small = no1 if no1<no2 else no2 

# when to use ternary ? 

# when we are using to obtain a single value we use ternary operator 

#Not for multiple operations like 


#WAP LCM :
#LCM means it has the highest value 

# no1,no2 = 3,9
# big = no1 if no1>no2 else no2 

# if big%no1==0 and big%no2==0:
#        print("LCM is ",big)



#LCM means it has the highest value 
# with no connected values
# no1,no2 = 3,7
# big = no1 if no1>no2 else no2 
# while True:
#        if big%no1==0 and big%no2==0:    #if is not a loop so using while 
#               print("LCM is ",big)
#               break
#        big +=1

#Prime Number

# no = int(input("Enter number  "))
# div =2 
# while div<no: 
#        if no%div ==0:
#               print("Not a prime")
#               break
#        div += 1
# else:
#        print("Prime")



#Write a program for Fibonacci series


# 0 1 1 2 3 5 8 13 


#Logic 👇
# f = 0
# s =1
# t = f+s
# print(t)

# f = s
# s = t 
# t = f+s 
# print(t)

# f = s
# s = t 
# t = f+s 
# print(t)


# f = 0
# s =1
# count = 1
# print(f)
# print(s)
# while count<10:
#        t = f +s
#        print(t)
#        f = s
#        s = t 
#        count +=1 

# If you want to take output Off the final final thing use else part
       
# f = 0
# s =1
# count = 1
# print(f)
# print(s)
# while count<10:
#        t = f +s
#        # print(t)
#        f = s
#        s = t 
#        count +=1 
# else:
#        print(t)


# In the in the about but we are 
# getting extraoutput soso we're going to 
# reduce The account by by changing if equal f to-1


# f = -1
# s =1
# count = 1

# while count<10:
#        t = f +s
#        print(t)
#        f = s
#        s = t 
#        count +=1 

#Write a program to make the to make it as user input


# f = -1
# s =1
# count = 1
# numb = int(input("Enter the Number: "))

# while count<numb:
#        t = f +s
#        print(t)
#        f = s
#        s = t 
#        count +=1 


# Write above program  a specific number is specified it should  break



# f = -1
# s =1
# count = 1
# # numb = int(input("Enter the Number: "))

# while count<count:
#        t = f +s
#        print(t)
#        if t == 34:
#               break
#        f = s
#        s = t 
#        count +=1 


#Simplest format 

# f =-1
# s =1 
# count =1
# while count<=8:
#        print(f+s)
#        s = f+s
#        f =s-f 
#        count +=1F


#1234 - > decimal 
#1234 / 10 -> 123.4 -->  
#1234%10 -> 4 reminder 
#1234//4 --> round off the quotient 







# a = 1234

# a= a//10  #round off the number 
# # a= a%10
# print(a)

#slicing operator only works on strings

# bread = 1234
# print(bread%10) #4 
# bread = bread //10 #123 
# print(bread)
# print(bread%10) #3
# bread = bread //10 #12
# print(bread)
# print(bread%10) #2
# bread = bread //10 #1 
# print(bread)
# print(bread%10) #!

#printing number in reverse order 

# bread = int(input("Enter the number: "))
# count = 0 
# while bread>0:
#        print(bread%10, end=" ") #it will show  the last digit
#        count +=1 
#        bread = bread //10  #it will round off the digits
# else:
#        print("\nCount of digit is ", count)


#printing the Addition of digits 

# bread = int(input("Enter the number: "))
# count = 0 
# total = 0
# while bread>0:
#        total = total + (bread%10) #it will show  the last digit
#        count +=1 
#        bread = bread //10  #it will round off the digits
# else:
#        print("Count of digit is ", count)
#        print("Addition  of digit is ", total)


#wap to for below eg 


#Reversed  of digit 

# 4+3 = 43 
#43+2 = 432 
#4*10 + 3 = 43
#43*10 + 2 = 

# bread = int(input("Enter the number: "))
# count = 0 
# total = 0
# while bread>0:
#        total = (total*10) + (bread%10) #it will show  the last digit
#        count +=1 
#        bread = bread //10  #it will round off the digits
# else:
#        print("Count of digit is ", count)
#        print("Reversed  of digit is ", total)



#palindrome 


# numb = int(input("Enter the Number:  "))
# no = numb
# rev = 0 
# while numb>0:
#        rev = (rev*10) + numb%10 #i this the value will be single value 
#        numb = numb //10 
# else:
#        print("Reverse value is ",rev)
#        if rev == no:
#               print("palindrome")
#        else:
#               print("Not palindrome ")

#Armstrong Number 

#SUM OF CUBES OF ITS DIGIT IS EQUAL TO THE NUMBER ITSELF 

#Eg 371 
# 3**3 + 7**3+1**1 = 371


# numb = int(input("Enter the Number:  "))
# no = numb
# total = 0 
# while numb>0:
#        dig = numb%10
#        digpower = dig*dig*dig 
#        total = total + digpower 
#        numb = numb//10  

# else:
#        if total == no:
#               print("Armstrong")
#        else:
#               print("Not Armstrong")


#WAP TO MAKE IT AS BINARY NUMBER  

# 1.GET NO FROM USER
# 2.DIVIDE THE NUMBER BY 2 
# 3. STORE REMAINDER 
# 4. NOW MAKE THE QUOTIENT AS NUMBER 
# 5. REPEAT STEP 2,3 AND 4 UNTILL QUOTIENT BECOMES 1 


#only works for 5 not for 4 
# no = 5 
# while no>0:
#        rem = no%2  #it will store the reminder 
#        print(rem,end ="")
#        no = no//2 #it will divide the quotient 


# no = 4
# binary = ''
# while no>0:
#        rem = no%2
#        binary = str(rem)+binary  #it will store the reminder 
       
#        no = no//2 

       

# for loop 

# name = input("What is your Email: ")
# for i in name:
#        if i>='a' and i <= 'z':
              
#               print(i,end="")

# name = input("What is your Email: ")
# for i in name:
#        if not (i>='a' and i <= 'z'):

#               print(i,end="")


#No of Alphabets present
# name = input("What is your statement : ")
# count = 0
# for i in name:
#        if i>='a' and i <= 'z':
#               count += 1
# else:
#        print("No of Alphabets present", count)


#No of Words present
# name = input("What is your statement : ")
# count = 0
# for i in name:
#        if i==' ':                           
#               count += 1
# else:
#        print("No of Words present", count+1)

#for in range 

# for  num in range(5):
#        print(num, end=' ')
# print()


# for num in range(1,5):
#        print(num, end = ' ')
# print()



# for num in range(1,5,2):
#        print(num, end = ' ')
# print()


# tables 

# no =1 
# for  num in range(3,31,3):
#        print(no," * 3 = ",num)
#        no+=1 

              