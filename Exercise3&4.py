import pandas

def price_finder(item):
    sum = 0
    item = item.lower().strip(' ')
    for letter in item:
        sum += (ord(letter)-96)
    return sum

# print(price_finder('bananas'))

cart = ['bananas', 'rice', 'paprika', 'potato chips']

def total(list):
    sum=0
    max_item = max(list, key=len)
    max_len = str(len(max_item))
    # not sure how to use this max_len in the string format
    for item in list:
        sum += price_finder(item)
        print('{:15}{:10}'.format(item, price_finder(item)))
    print('-------------------------')
    print('Total{:20}'.format(sum))
    return sum

(total(cart))