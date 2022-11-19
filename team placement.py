import math
num = int(input('please inter number of students: '))
numbers = []
number = input(f'enter {num} students records: ')
number = number.split()
while len(number)!=num:
    print("you've entered wrong amount of numbers.")
    number = input('inter numbers again: ')
    number= number.split()
for item in number:
    numbers.append(int(item))
for i in numbers:
    if i>=3:
        numbers.remove(i)
if len(numbers)<3:
    print("sorry you cant form a team with these students")
if len(numbers)==3:
    print('you can make only one team')
else:
    answer = (math.factorial(len(numbers)))/(math.factorial(len(numbers)-3))
    print(f' you can make {int(answer)} different teams.')