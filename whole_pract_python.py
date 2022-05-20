  #(decision making) if , elif , nasted if
# for loop range (only int used also indexing num) , variable  "only used variable name"
name = 'python programming'
variable = 'python'
if variable not in name:
    print('yes')
    print(len(name))
    if 'a' in variable:
        print('yes')
    elif 'm' in variable:
        print('yes')
    elif 'y' in name:
        print('yes')
    else:
        print('no')
else:
    print('complete programming')

list = [(1,7),(3,8),(4,6)] # to print 7,8,6
print(len(list))
for num in range(len(list)):
    print(list[num][1])

for x in list:   # another method
    print(x[1])


variable = 'python programming'
for name in range(len(variable)):
    print((variable[name]))
for name in variable:
    print(name)

#prime numbers between 100
'''for primes in range(1,100):
    if primes % 2 == 1 or not primes == 2:
        print('prime number : ',primes)
    else:
        print('not a prime number', primes)'''

#also use while condition to  find prime number between 100
num = 1
while num <= 100:
    if num % 2 ==1 or num == 2:
        print('prime number : ',num)
    else:
        print('not a prime number : ',num)
    num += 1

#to find sum of 100 numbers
total = 0
num = 0
while num <=100:
    total = num+total
    num += 1
    print(num,'+' ,total,'=' ,total)

#factors of numbers

def user_define(x):
    print('the factors of', x, 'are : ')
    for i in range(1,x+1):
         if (x % i) == 0:  # factors condition
            print(i)
num = 320
user_define(num)

#break , continue , pass
list =  [10,20,30,60,50,57,58,70,90,100]
for numbers in list:
    if numbers == 50:
        pass
        print('condition pass')
    print(numbers)
#functions
def greets(name):

    print('hi hello '+ name +' good morning')
greets('kalyan')

#to find avg  marks using function

def avg_marks(marks):
    total_no_subjects = len(marks)
    sum_marks = sum(marks)
    find_avg_marks = sum_marks/total_no_subjects
    return find_avg_marks
#calculate grade
def compute_grade(find_avg_marks):
    if find_avg_marks >= 80:
        grade = 'A'
    elif find_avg_marks >=60:
        grade = 'B'
    elif find_avg_marks>=50:
        grade = 'C'
    else:
        grade = 'D'
    return grade

marks = [50,62,89,67,53,47.74]
find_avg_marks = avg_marks(marks)
print('the avg marks :', round(find_avg_marks))
grade = compute_grade(find_avg_marks)
print("your grade : ",grade)

#adding and multiplying of two number

def adding_num(a,b):     #adding of two numbers
    return a+b
a = 50
b = 60
add = adding_num(a,b)
print('adding of two numbers :',add)
def multip_num(a,b):   # multiply two numbers
    return a*b
product = multip_num(a,b)
print('product of num :',product)

#to check prime number or not


my_list = int(input('enter your num : '))
for x in range(2,my_list):
    if my_list % x == 0:
        print('not prime',my_list,end=' ')
        break

else:
    print('prime',my_list,end=' ')
