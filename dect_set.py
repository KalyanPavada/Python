# use of sets
s = {10,20,30,50,'python'}
d = {10,20,30,50,'python','kalyan'}
add_d = 'name','age'
d.issuperset(s)
d.difference_update(s)
d.intersection_update(s)
print(d)
s.add(add_d)
print(d)

#take dict and add these elements in sets

person = {'name':'laxmi','age':25,'salary':1000}
for k in person.keys():
    print(k)
for v in person.values():
    print(v)
k = person.update()
v = person.values()
print(k)
print(v)
print(person)
my_set = set()
my_set.update(person.items())  # dict values convert to set()

print(my_set)

#use of function

#num=100 to 500 prime numbers
for x in range(100,500):
    for i in range(2,x):
        if x % i ==0:
            print("not a prime",x)
            break
    else:
        print("prime num",x)
#
num = int(input('enter your num : '))
def my_fact(num):
    if num == 0 or num ==1:
        return 1
    else:
        return num*my_fact(num-1)


f = my_fact(num)
print(f)


a = [10,20,30,50,4,5,50,5,90,40,60]

x = (len(a))
y = sum(a)
avg = round(y/x)
print('my length: {} \nmy sum: {} \nmy avg : {}'.format(x,y,avg))




