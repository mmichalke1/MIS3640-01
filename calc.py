import math
# The volume of a sphere with radius r is
# (4/3)πr3. What is the volume of a sphere with radius 5?
pi = math.pi
r = 5
volume = (4/3)*pi*r**3
print('The volume of a sphere with a radius of 5 is {:.2f}.'.format(volume))

# Suppose the cover price of a book is $24.95, but bookstores get a 40\% discount. Shipping costs $3 for the first copy
# and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

price = 24.95
discount = .4
shipping_1 = 3
shipping_n = .75
n = 60 #number of copies sold

total_cost = (price*discount*n) + shipping_1 + (shipping_n*(n-1))
print('The total cost of the order would be ${:.2f}.'.format(total_cost))

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile)
# and 1 mile at easy pace again, what time do I get home for breakfast?

import datetime
mile_1 = datetime.timedelta(minutes=8, seconds=15)
mile_2 = datetime.timedelta(minutes=7, seconds=12)

trip_time = mile_1*2 + mile_2*3

begin_time = datetime.timedelta(hours=6, minutes=52)
end_time = begin_time + trip_time
print('You would arrive home at {} for breakfast'.format(end_time))




# If my average grade rises from 82 to 89. What is the percentage of the increase? Format the result as 'xx.x%'. Keep one
# figure after decimal point.

grade1 = 82
grade2 = 89
percent_increase = ((grade2-grade1)/grade1)*100
print('My grades increased by {:04.1f}%'.format(percent_increase))
