operation = input('''please type in the match operation you would like to complete 
+ for addition 
- for subtraction 
* for multiplication 
/ for division 
''') 

number_1 = int(input('Enter you first number: '))
number_2 = int(input('Enter you first number: '))

if operation == '+': 
    print('{} + {} = '.format(number_1, number_2)) 
    print(number_1 + number_2)

elif operation == "-":
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2) 

elif operation == "*":
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2) 

elif operation == "/":
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2) 

else: 
    print ('you have not typed a valid operator, please run the program again.')
