'''Write a program that prints out the multiplication table of the entered number by the user by using for loop.

Example 1:
>>>
5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

'''
#code:


num = int(input())
for i in range(1,11):
    print(num, "x", i, "=", num*i)


'''Write a program that asks a user to enter a number and print out how many numbers from 1 to N (including N) are divisible by 5 or 7 and the list of the numbers using for loop.

Example:
>>>
40                                                                  
There are 12 numbers divisible by 5 and 7.
5,7,10,14,15,20,21,25,28,30,35,40,                  
 '''

#code:

def divisible(num):
    if int(num):
        if (int(num) / 5).is_integer() or (int(num) / 7).is_integer():
            return True
    return False

def remove_special_chars(thisString):
    return (''.join(e for e in thisString if e.isalnum()))

def check_int(num):
    if num.isdigit():
        return int(num)
    else:
        print("Input is not a number!")
        exit(1)


num = input()
num = remove_special_chars(num)
num = check_int(num)

numbers = []
thisNum = 1

for thisNum in range(0, num+1):
    if divisible(int(thisNum)):
        numbers.append(int(thisNum))
    thisNum += 1

print(numbers)
print("There are", len(numbers), "numbers divisible by 5 or 7" )

'''Write a program that asks a user to enter a number and print out the sum of the powers of 2 from 0 to N using for loop.

SUM = 20 + 21+22+...+2N

Example:
>>>
4
The sum is 31.
>>>
2
The sum is 7.
'''

#code:
def remove_special_chars(thisString):
    return (''.join(e for e in thisString if e.isalnum()))

def check_int(num):
    if num.isdigit():
        return int(num)
    else:
        print("Input is not a number!")
        exit(1)

def get_power_of_2(power):
    return (2**power)

num = input()
num = remove_special_chars(num)
num = check_int(num)

result = 0
thisNum = 0

for thisNum in range(0, num+1):
    result = result + get_power_of_2(thisNum)
    thisNum += 1

print('The sum is', result)



'''Write a program that asks a user to enter a number and print out the squares of a number (using while loop ).

12 , 22 , 32 , 42 , 52 , 62 , 72 , 82 , 92 ,...., N2 ====> 1, 4, 9, 16, 25, 36, 49, 64, 81, ... , N*N

Example 1:
>>>
4
1,4,9,16,
Example 2:
>>>
8
1,4,9,16,25,36,49,64,
'''
#code:

def remove_special_chars(thisString):
    return (''.join(e for e in thisString if e.isalnum()))

def check_int(num):
    if num.isdigit():
        return int(num)
    else:
        print("Input is not a number!")
        exit(1)

num = input()
num = remove_special_chars(num)
num = check_int(num)

numbers = []
thisNum = 1

if num == 0:
    print(0)
    exit()

while thisNum != int(num)+1:
    numbers.append(int(thisNum**2))
    thisNum += 1


print(numbers)

'''Write a program that asks a user to enter a number and print out factorial of this number using for loop.

N! = 1 × 2 × 3 × . . . × N

Example:
>>>
Enter a number: 5                                                                         		
Factorial of 5 is 120.
>>>
Enter a number: 0
Factorial of 0 is 1. 
'''

#code:
def remove_spaces(thisString):
    # Using .replace() to replace " " <-space with "" <- nothing
    return (thisString.replace(" ", ""))

def check_positive_int(num):
    if num.isdigit():
        if int(num) >= 0:
            return int(num)
    else:
        if int(num) < 0:
            print("Negative integer.")
            exit(1)

num = input()
num = remove_spaces(num)
num = check_positive_int(num)

factorial = 1

for thisNum in range(1, num+1):
    factorial = factorial * thisNum

print ("Factorial of %i is %i." % (num, factorial))


'''Write a program that asks user to enter a base and its power. Find the power of a number using for loop.

Картинки по запросу base and power

Example:
>>>
Enter a base: 8
Enter a power: 2  
The answer is 64.'''

#code:(still didn't fix)
def remove_special_chars(thisString):
    return (''.join(e for e in thisString if e.isalnum()))

def check_int(num):
    if num.isdigit():
        return int(num)
    else:
        print("Input is not a number!")
        exit(1)

base = input()
power = input()

base = remove_special_chars(base)
power = remove_special_chars(power)


base = check_int(base)
power = check_int(power)


result = int(base)

for i in range(1, int(power)):
    result = result * base

print('The answer is %i.' % (result))