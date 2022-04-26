# find the train berth

my_berth = int(input('enter your bearth num : '))
def train_berth():
    if my_berth % 8 == 1 or  my_berth % 8 == 4:
        print('its lower berth:',my_berth)
    elif my_berth % 8 == 2 or my_berth % 8 == 5:
        print('its middle berth: ',my_berth)
    elif my_berth % 8 == 3 or my_berth % 8 == 6:
        print('its upper berth : ',my_berth)
    elif my_berth % 8 == 7 :
        print('its side lower berth : ',my_berth)
    else:
        print('its side upper berth : ',my_berth)

train_berth()
