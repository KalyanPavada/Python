
# num = int(input('enter your number : '))
def find_fact(num):                 # find factorial from user require
    if num == 0 or num == 1:
        return 1
    else:
        return num*find_fact(num-1)

# f = my_fact(num)
# print('factorial of {}:'.format(num),f)

def find_avg(user_req):      # find avg from user require
    num_sub = len(user_req)
    sum_sub = sum(user_req)
    my_avg = sum_sub/num_sub
    return my_avg
#avg = find_avg(50,60,42,82,90)
#print('avg of ', avg)

#num = int(input('enter your num : '))
def find_prime(num):
    for i in range(2,num+1):
        if num % i == 0:
            return 'its not prime'
            # print('its not prime', num)
            # print(i, 'times of', num // i, 'is', ':', num)
            # break

        else:
            return 'its prime'
            # print('its a prime',num)

#find_prime(num)



