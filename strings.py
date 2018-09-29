team = 'New England Patriots'
# print(len(team))

letter = team[1]
# print(letter)
###[] shows the index
# print(team[-20])

###Traversal with a for loop
# index=0
# while index < len(team):
#     letter = team[index]
#     print(letter)
#     index = index + 1
### For Loop is better for this
# for letter in team:
#     print(letter)

# prefixes = 'JKLMNOPQ'
# suffic = 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter =='Q':
#         print(letter + 'u' + suffic)
#     else:
#         print(letter+suffic)
#
# for i in range(len(team)):
#     if team[i] =='a':
#         print(i)
#
# for i, letter in enumerate(team):
#     if letter == 'a':
#         print(i, letter)

def count(s, letter):
    count = 0
    for x in s:
        if x == letter:
            count += 1
    return count

print(count(team, 'a'))
